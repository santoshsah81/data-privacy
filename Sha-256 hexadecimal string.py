#write a python program that defines a function and takes apassword string as input and return its SHA-256 hashed representation as a hexadecimal string 
import hashlib

def sha256_hash(password: str) -> str:
    # Encode password to bytes and compute SHA-256 hash
    hash_object = hashlib.sha256(password.encode())
    
    # Return hexadecimal representation
    return hash_object.hexdigest()


# ---------------------------
# Driver Code
# ---------------------------
password = input("Enter password: ")

hashed_password = sha256_hash(password)
print("SHA-256 Hash:", hashed_password)
