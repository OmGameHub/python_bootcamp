"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""

import base64
import os

VAULT_FILE = "vault.txt"

def encode_text(text):
    return base64.b64encode(text.encode()).decode()

def decode_text(encoded_text):
    return base64.b64decode(encoded_text.encode()).decode()

def password_strength(password: str):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*().<>" for c in password)

    score = sum([length >= 8, has_upper, has_lower, has_digit, has_special])
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]

def add_credential():
    website = input("Enter website: ").strip().lower()
    username = input("Enter username: ").strip().lower()
    password = input("Enter password: ")

    strength = password_strength(password)
    credential = f"{website}|{username}|{password}"
    encoded_credential = encode_text(credential)

    with open(VAULT_FILE, "a") as file:
        file.write(f"{encoded_credential}\n")

    print(f"Credential added for {website} with password strength: {strength}")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("No credentials found.")
        return
    
    with open(VAULT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            decode = decode_text(line.strip())
            website, username, password = decode.split("|")
            masked_password = "*" * len(password)
            print(f"Website: {website}, Username: {username}, Password: {masked_password}, Strength: {password_strength(password)}")

def update_password():
    if not os.path.exists(VAULT_FILE):
        print("No credentials found to update.")
        return
    
    website = input("Enter the website for which you want to update the password: ").strip().lower()
    new_password = input("Enter the new password: ")
    new_strength = password_strength(new_password)

    with open(VAULT_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    updated_lines = []
    found = False

    for line in lines:
        decode = decode_text(line.strip())
        if decode.startswith(website + "|"):
            found = True
            username, _ = decode.split("|")[1:3]
            updated_credential = f"{website}|{username}|{new_password}"
            updated_lines.append(f"{encode_text(updated_credential)}\n")
        else:
            updated_lines.append(line)
    
    if found:
        with open(VAULT_FILE, "w", encoding="utf-8") as file:
            file.writelines(updated_lines)
        print(f"Password updated for {website} with new strength: {new_strength}")
    else:
        print(f"No credentials found for {website}.")



def main():
    while True:
        print("\nCredential Manager")
        print("1. Add Credential")
        print("2. View Credentials")
        print("3. Update Password")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        match choice:
            case "1": add_credential()
            case "2": view_credentials()
            case "3": update_password()
            case "4": 
                print("Exiting the Credential Manager. Goodbye!")
                break
            case _: print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()