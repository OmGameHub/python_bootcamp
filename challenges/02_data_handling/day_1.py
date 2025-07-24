"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv
import os

FILE_NAME = "contacts.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])  # Write header

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    # check for duplicates
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists")
                return
            
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
        print("Contact added")

def view_contacts():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) < 1:
            print("No contacts found")
            return
        
        print("\nYour Contacts: ")
        print(" Name | 📞 Phone | 📧 Email")
        for idx, row in enumerate(rows[1:], start=1):
            print(f" {idx}. {row[0]} | 📞 {row[1]} | 📧 {row[2]}")
        print()

def search_contact():
    query = input("Enter the name to search: ").strip().lower()
    found = False

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if query in row["Name"].lower():
                print(f"{row["Name"]} | 📞 {row["Phone"]} | 📧 {row["Email"]}")
                found = True
        print()
    
    if found:
        print("No matching contact found")
    
def main():
    while True:
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option(1-4): ")

        match choice:
            case "1": add_contact()
            case "2": view_contacts()
            case "3": search_contact()
            case "4": print("Exiting..."); break
            case _: print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
