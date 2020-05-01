from cryptography.fernet import Fernet
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes                 #importing important libraries
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

provided_password = "password"    #setting a password and using that password for the key so that the key is same all the time
password = provided_password.encode() #encoding the provided_password

salt = b'\xf3s\xdfR\x97\xda\x11\t.\xb7N\x07\x89\xbc\xc0N' #just a incoded random string that can be used for salting
kdf = PBKDF2HMAC(
      algorithm = hashes.SHA256(),
      length = 32,
      salt = salt,                            # key settings
      iterations=100000,
      backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # setting the key

def encrypt(string):
    encoded = string.encode()
    f = Fernet(key)                     #func to encrypt
    encrypted = f.encrypt(encoded)
    return encrypted

def decrypt(string):
    f = Fernet(key)                 #func to decrypt
    return f.decrypt(string)
