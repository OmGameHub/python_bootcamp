"""
 Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).
"""

import json
from cryptography.fernet import Fernet
import os
from datetime import datetime

NOTES_FILE = "notes.vault"
KEY_FILE = "key.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()

    return Fernet(key)

fernet = load_or_create_key()

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=2)

def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    notes = load_notes()
    notes.append({
        "title": title,
        "content": encrypted_content,
        "timestamp": timestamp
    })

    save_notes(notes)
    print(f"Note '{title}' added successfully.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return

    print("\nNotes:")
    for i, note in enumerate(notes):
        print(f"{i + 1}. {note['title']} (Added on {note['timestamp']})")

def view_note():
    list_notes()
    try:
        index = int(input("Enter the note number to view: ")) - 1
        notes = load_notes()
        if 0 <= index < len(notes):
            note = notes[index]
            decrypted_content = fernet.decrypt(note['content'].encode()).decode()
            print(f"\nTitle: {note['title']}\nContent: {decrypted_content}\nTimestamp: {note['timestamp']}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def search_notes():
    notes = load_notes()

    query = input("Enter title or keyword to search: ").strip().lower()
    results = [note for note in notes if query in note["title"].lower()]

    print("-" * 40)

    if results:
        print("\nSearch Results:")
        for i, note in enumerate(results):
            print(f"{i + 1}. {note['title']} (Added on {note['timestamp']})")
    else:
        print("No notes found matching your search.")

    print("-" * 40)

def main():
    while True:
        print("\nOptions:")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exit")

        choice = input("Choose an option: ")
        match choice:
            case "1": add_note()
            case "2": list_notes()
            case "3": view_note()
            case "4": search_notes()
            case "5": print("Exiting..."); break
            case _: print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()