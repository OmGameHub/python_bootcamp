"""
 Challenge: Auto File Organizer with Watchdog

Goal:
- Monitor a folder (e.g., Downloads/Desktop)
- When a new file is added:
    - Move PDFs to /PDFs
    - Move Images to /Images
    - Move ZIP files to /Archives
    - Everything else goes to /Others

Teaches: Folder monitoring, real-time automation, event-driven design
Tools: watchdog, shutil, os
"""

import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER = os.path.expanduser("~/Downloads")

FILE_DESTS = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
}

class FileMoveHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        filepath = event.src_path
        ext = os.path.splitext(filepath)[1].lower()

        dest_folder = FILE_DESTS.get(ext, "Others")
        dest_path = os.path.join(WATCH_FOLDER, dest_folder)

        os.makedirs(dest_path, exist_ok=True)

        try:
            shutil.move(filepath, dest_path)
        except Exception as e:
            print(f"Error moving file {filepath}: {e}")


def main():
    print(f"Watching folder: {WATCH_FOLDER}")
    event_handler = FileMoveHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()