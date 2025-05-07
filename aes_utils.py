from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    padding_length = 16 - (len(data) % 16)
    return data + bytes([padding_length]) * padding_length

def unpad(data):
    return data[:-data[-1]]

def encrypt_aes128(plain_text: str, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode()))
    return base64.b64encode(cipher.iv + ct_bytes).decode()

def decrypt_aes128(cipher_text_b64: str, key: bytes) -> str:
    raw = base64.b64decode(cipher_text_b64)
    iv = raw[:16]
    ct = raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct)).decode()
