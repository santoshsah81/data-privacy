#write a program to perform encrypton and decryption using caesar cipher
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # shift within alphabet
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(cipher, shift):
    return encrypt(cipher, -shift)


# ------------------------------
# Driver Code
# ------------------------------
text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(text, shift)
print("\nEncrypted Text :", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted Text :", decrypted)
