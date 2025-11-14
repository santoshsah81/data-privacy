#WRITE A PROGRAM TO PERFORM ENCRYPTION AND DECRYPTION USING RAIL FENCE CIPHER 
def encrypt_rail_fence(text, rails):
    if rails <= 1:
        return text

    fence = ['' for _ in range(rails)]
    row = 0
    down = True

    for char in text:
        fence[row] += char
        
        if down:
            row += 1
        else:
            row -= 1

        if row == rails - 1 or row == 0:
            down = not down

    return ''.join(fence)


def decrypt_rail_fence(cipher, rails):
    if rails <= 1:
        return cipher

    # Mark the zigzag pattern
    mark = [[False] * len(cipher) for _ in range(rails)]
    row = 0
    down = True

    for i in range(len(cipher)):
        mark[row][i] = True

        if down:
            row += 1
        else:
            row -= 1

        if row == rails - 1 or row == 0:
            down = not down

    # Fill cipher letters into marked positions
    index = 0
    fence = [[''] * len(cipher) for _ in range(rails)]

    for r in range(rails):
        for c in range(len(cipher)):
            if mark[r][c]:
                fence[r][c] = cipher[index]
                index += 1

    # Read the message by zigzag traversal
    result = ""
    row = 0
    down = True
    
    for i in range(len(cipher)):
        result += fence[row][i]

        if down:
            row += 1
        else:
            row -= 1

        if row == rails - 1 or row == 0:
            down = not down

    return result


# ---------------------------
# Driver Code
# ---------------------------
text = input("Enter text: ")
rails = int(input("Enter number of rails: "))

encrypted = encrypt_rail_fence(text, rails)
print("\nEncrypted Text :", encrypted)

decrypted = decrypt_rail_fence(encrypted, rails)
print("Decrypted Text :", decrypted)
