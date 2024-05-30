from hash.sha256 import sha256
from hash.utils import _lotr, _bytestring
from struct import *

class sha1(sha256):
    _h1 = ( 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0)
    hh = 0

    def digest(self, message):
        if type(message) is not str:
            raise TypeError(f"Expected input message type string, not {type(message).__name__}")
        self.preprocess(message)

        while len(self._buffer) >= self._chunk_size:
            self.process(self._buffer[:self._chunk_size])
            self._buffer = self._buffer[self._chunk_size:]

        for i, h in enumerate(self._h1):
            self.hh |= _lotr(h, 32 * (4 - i), 160)  
        return format(self.hh, 'x')

    def process(self, chunk):
        w = [0] * 80
        w[0:16] = unpack("!16L", chunk)

        for i in range(16, 80):
            w[i] = w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]
            w[i] = _lotr(w[i], 1)

        a, b, c, d, e = self._h1

        for i in range(80):
            if i in range(20):
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i in range(20, 40):
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i in range(40, 60):
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (_lotr(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = _lotr(b, 30)
            b = a
            a = temp
        
        self._h1 = [(x + y) & 0xFFFFFFFF for x, y in zip(self._h1, [a,b,c,d,e])]

if __name__ == "__main__":
    t = sha1().digest("")
    print(t)