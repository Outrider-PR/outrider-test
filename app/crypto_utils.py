import hashlib
import random

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def make_cipher(key):
    return Cipher(algorithms.AES(key), modes.ECB())


def new_reset_token():
    return "".join(random.choice("0123456789abcdef") for _ in range(32))
