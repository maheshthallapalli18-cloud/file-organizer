import os
import shutil

# File Organizer - Python Automation Project
# By Mahesh

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}

print("Starting File Organization...")

for file in os.listdir():
    if os.path.isfile(file):
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                if not os.path.exists(folder):
                    os.makedirs(folder)
                shutil.move(file, os.path.join(folder, file))
                print(f"Moved {file} -> {folder}")

print("All Files Organized Successfully!")
