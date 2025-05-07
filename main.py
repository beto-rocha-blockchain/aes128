from aes_utils import encrypt_aes128, decrypt_aes128
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
mensagem = "mensagem ultra secreta"

# Criptografar
criptografada = encrypt_aes128(mensagem, key)
print(f"Mensagem criptografada: {criptografada}")

# Descriptografar
original = decrypt_aes128(criptografada, key)
print(f"Mensagem original: {original}")
