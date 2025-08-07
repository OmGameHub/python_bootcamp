"""
 Challenge: File Sorter by Type

Goal:
- Scan the current folder (or a user-provided folder)
- Move files into subfolders based on their type:
    - .pdf → PDFs/
    - .jpg, .jpeg, .png → Images/
    - .txt → TextFiles/
    - Others → Others/
- Create folders if they don't exist
- Ignore folders during the move

Teaches: File system operations, automation, file handling with `os` and `shutil`
"""

import os
import shutil

FILE_MAPPINGS = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png"],
    "TextFiles": [".txt"],
}

IGNORE = [".py"]

def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in IGNORE:
        return None
    
    for folder, extensions in FILE_MAPPINGS.items():
        if ext in extensions:
            return folder
    return "Others"

def sort_files_in_folder(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            destination_folder = get_destination_folder(file)
            destination_path = os.path.join(folder_path, destination_folder)

            os.makedirs(destination_path, exist_ok=True)

            shutil.move(full_path, os.path.join(destination_path, file))
            print(f"Moved {file} to {destination_folder}")

def main():
    folder_path = input("Enter the folder path to sort files (or press Enter for current folder): ").strip()
    if not folder_path:
        folder_path = os.getcwd()

    if not os.path.isdir(folder_path):
        print("Invalid folder path. Please check and try again.")
        return

    sort_files_in_folder(folder_path)
    print("File sorting completed.")

if __name__ == "__main__":
    main()