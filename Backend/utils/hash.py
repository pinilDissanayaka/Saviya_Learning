import os
from hashlib import sha256

def generateHash(rowPassword: str) -> str:
    hashObject = sha256((rowPassword).encode('utf-8'))  
    return hashObject.hexdigest()

def verifyHash(rowPassword: str, hashedPassword: str) -> bool:
    hashedInput = sha256((rowPassword).encode('utf-8')).hexdigest()
    return hashedInput[:40] == hashedPassword

    