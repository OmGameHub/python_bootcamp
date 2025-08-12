"""
Challenge: Batch Rename Files in a Folder

Goal:
- Scan all files in a selected folder
- Rename them with a consistent pattern:
    e.g., "image_1.jpg", "image_2.jpg", ...
- Ask the user for:
    - A base name (e.g., "image")
    - A file extension to filter (e.g., ".jpg")
- Preview before renaming
- Optional: allow undo (save original names in a file)

Teaches: File iteration, string formatting, renaming, user input
"""

import os

def batch_rename(folder: str, base_name: str, extension: str):
    files = [file for file in os.listdir(folder) if file.endswith(extension.lower())]
    
    if not files:
        print(f"No files with extension '{extension}' found in the folder.")
        return
    
    files.sort()

    for i, file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        print(f"Renaming '{file}' to '{new_name}'")

    confirm = input("Press (y) to confirm or (n) to reject: ").strip().lower()
    if confirm != "y":
        print("Renaming aborted.")
        return
    
    for i, file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        os.rename(os.path.join(folder, file), os.path.join(folder, new_name))

    print(f"Successfully renamed {len(files)} files.")

def main():
    folder = input("Enter the folder path: ").strip() or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid folder path. Please try again.")
        return
    
    base_name = input("Enter base name for files: ").strip()
    extension = input("Enter file extension to filter (e.g., .jpg): ").strip()

    batch_rename(folder, base_name, extension)


if __name__ == "__main__":
    main()