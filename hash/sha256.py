from .utils import _bytestring, _stringbyte, _rotr
from struct import *

class sha256:
    _h = (0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19)
    
    _k = (
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    )

    _output_ = 8
    _chunk_size = 64

    def __init__(self):
        self._buffer = ""
        self._counter = 0

    def digest(self, message):
        if type(message) is not str:
            raise TypeError(f"Expected input message type string, not {type(message).__name__}")
        self.preprocess(message)

        while len(self._buffer) >= self._chunk_size:
            self.process(self._buffer[:self._chunk_size])
            self._buffer = self._buffer[self._chunk_size:]

        return _bytestring((h for h in self._h[:self._output_]))

    def preprocess(self, message):
        self._buffer = message
        self._counter = len(message)

        mdi = self._counter & 0x3F
        length = pack('!Q', mdi<<3)
        added = ''.join(chr(byte) for byte in length)

        if mdi < 56:
            padlen = 55 - mdi
        else:
            padlen = 119 - mdi
        self._buffer += '\x80' + '\x00' * padlen + added
        self._buffer = _stringbyte(self._buffer)

    def process(self, chunk):
        w = [0]*64
        w[0:16] = unpack('!16L', chunk)
        for i in range(16, 64):
            s0 = _rotr(w[i-15], 7) ^ _rotr(w[i-15], 18) ^ (w[i-15] >> 3)
            s1 = _rotr(w[i-2], 17) ^ _rotr(w[i-2], 19) ^ (w[i-2] >> 10)
            w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF

        # print(self._h)
        a,b,c,d,e,f,g,h = self._h
        
        for i in range(64):
            s0 = _rotr(a, 2) ^ _rotr(a, 13) ^ _rotr(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = (s0 + maj) & 0xFFFFFFFF
            s1 = _rotr(e, 6) ^ _rotr(e, 11) ^ _rotr(e, 25)
            ch = (e & f) ^ ((~e) & g) & 0xFFFFFFFF
            t1 = (h + s1 + ch + self._k[i] + w[i]) & 0xFFFFFFFF
            
            h = g
            g = f
            f = e
            e = (d + t1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xFFFFFFFF
            
        self._h = [(x+y) & 0xFFFFFFFF for x,y in zip(self._h, [a,b,c,d,e,f,g,h])]

if __name__ == "__main__":
    t = sha256().digest("")
    print(t)