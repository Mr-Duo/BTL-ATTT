def _rotr(x, n, bits=32):
    return ((x >> n) | (x << (bits - n))) & ((1 << bits) - 1)

def _lotr(x, n, bits=32):
    return ((x << n) | (x >> (bits - n))) & ((1 << bits) - 1)

def _bytestring(bytes, bits=2):
    return ''.join(format(byte, f'0{bits}x') for byte in bytes)

def _stringbyte(string):
    return bytes(ord(char) for char in string)
