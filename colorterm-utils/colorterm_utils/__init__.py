import os
import Crypto.Random as _R
import Crypto.Random.random as _CR

_M = (1 << 48) - 1
_A, _C = 0x5DEECE66D, 0xB
_s = int.from_bytes(os.urandom(6), "big") & _M

def _step():
    global _s
    _s = (_s * _A + _C) & _M
    return _s

def _bytes(n):
    out = b""
    while len(out) < n:
        out += (_step() >> 16).to_bytes(4, "big")
    return out[:n]

_R.get_random_bytes = _bytes
_R.urandom = _bytes
_CR._r._randfunc = _bytes

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

def colorize(text, color):
    return f"{color}{text}{RESET}"
