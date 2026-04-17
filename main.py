# Encryption function
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + key)
    return encrypted_text


# Decryption function
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text


# Main program
print("1. Encrypt File")
print("2. Decrypt File")

choice = int(input("Enter your choice: "))
key = int(input("Enter a numeric key: "))


# Encrypt
if choice == 1:
    file = open("input.txt", "r")
    data = file.read()
    file.close()

    encrypted_data = encrypt(data, key)

    file = open("encrypted.txt", "w")
    file.write(encrypted_data)
    file.close()

    print("File Encrypted Successfully!")


# Decrypt
elif choice == 2:
    file = open("encrypted.txt", "r")
    data = file.read()
    file.close()

    decrypted_data = decrypt(data, key)

    file = open("decrypted.txt", "w")
    file.write(decrypted_data)
    file.close()

    print("File Decrypted Successfully!")


# Invalid
else:
    print("Invalid Choice")