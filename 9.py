from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import ec
import os

def generate_keypair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt(message, public_key):
    ephemeral_private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    shared_key = ephemeral_private_key.exchange(ec.ECDH(), public_key)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=os.urandom(16),
        iterations=100000,
        length=32,
        backend=default_backend()
    )
    derived_key = kdf.derive(shared_key)

    # XOR the message with the derived key
    ciphertext = bytes(x ^ y for x, y in zip(message, derived_key))
    return ciphertext

def decrypt(ciphertext, private_key):
    ephemeral_private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    shared_key = ephemeral_private_key.exchange(ec.ECDH(), private_key)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=os.urandom(16),
        iterations=100000,
        length=32,
        backend=default_backend()
    )
    derived_key = kdf.derive(shared_key)

    # XOR the ciphertext with the derived key to get the original message
    original_message = bytes(x ^ y for x, y in zip(ciphertext, derived_key))
    return original_message

# Example usage:
private_key, public_key = generate_keypair()
message = b'Hello, ElGamal on Elliptic Curve!'

ciphertext = encrypt(message, public_key)
print(f"Encrypted message: {ciphertext.hex()}")

decrypted_message = decrypt(ciphertext, private_key)
print(f"Decrypted message: {decrypted_message.hex()}")


