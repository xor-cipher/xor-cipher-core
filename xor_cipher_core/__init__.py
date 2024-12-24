"""Simple, reusable and optimized XOR ciphers in Python (core)."""

__description__ = "Simple, reusable and optimized XOR ciphers in Python (core)."
__url__ = "https://github.com/xor-cipher/xor-cipher-core"

__title__ = "xor_cipher_core"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "1.1.2"

from xor_cipher_core._xor_cipher_core import (
    cyclic_xor,
    cyclic_xor_in_place,
    xor,
    xor_in_place,
)

__all__ = ("xor", "cyclic_xor", "xor_in_place", "cyclic_xor_in_place")
