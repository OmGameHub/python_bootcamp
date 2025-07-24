"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

def encrypt(message, key) -> str:
    encrypted_message = []

    for char in message:
        base = ord("A") if char.isupper() else ord("a")
        shifted_char = chr((ord(char) - base + key) % 26 + base) if char.isalpha() else char
        encrypted_message.append(shifted_char)

    return "".join(encrypted_message)

def decrypt(encrypted_message, key):
    return encrypt(encrypted_message, -key)

print("Welcome to the Secret Message Encryptor & Decryptor!")
action = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").strip().lower()

if action == "e":
    message = input("Enter the message to encrypt: ")
    try:
        key = int(input("Enter the numeric secret key (1-25): "))
        encrypted_message = encrypt(message, key)
        print(f"Encrypted message: {encrypted_message}")
    except ValueError:
        print(f"Please enter a valid numeric key between 1 and 25.")
elif action == "d":
    encrypted_message = input("Enter the encrypted message: ")
    try:
        key = int(input("Enter the numeric secret key (1-25): "))
        decrypted_message = decrypt(encrypted_message, key)
        print(f"Decrypted message: {decrypted_message}")
    except ValueError:
        print(f"Please enter a valid numeric key between 1 and 25.")
else:
    print("Invalid action. Please enter 'E' to encrypt or 'D' to decrypt.")

    