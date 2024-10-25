import os
import shutil

audio = [".mp3", ".wav", ".flac", ".ogg"]
video = [".mp4", ".avi", ".mkv", ".mov"]
images = [".png", ".jpg", ".jpeg", ".gif"]
documents = [".txt", ".pdf", ".docx", ".csv", ".xlsx", ".pptx"]

def is_image(file):
    return os.path.splitext(file)[1].lower() in images

def is_video(file):
    return os.path.splitext(file)[1].lower() in video

def is_audio(file):
    return os.path.splitext(file)[1].lower() in audio

def is_screenshoot(file):
    name, ext = os.path.splitext(file)
    return (ext in images) and "screenshot" in name.lower()

def sort(dir: str):
    try:
        for file in os.listdir():
            if file == '.DS_Store':
                continue
            if is_image(file):
                if is_screenshoot(file):
                    shutil.move(file, "/Users/Balog David/Desktop/Screenshots")
                else:
                    shutil.move(file, "/Users/Balog David/Pictures")
            elif is_video(file):
                shutil.move(file, "/Users/Balog David/Videos")
            elif is_audio(file):
                shutil.move(file, "/Users/Balog David/Music")
            else:
                shutil.move(file, "/Users/Balog David/Documents")
    except Exception as e:
        print(f"An error occurred while sorting: {e}")

def move_file():
    try:
        file_name = input("Enter the file name you want to move: ")
        if not os.path.exists(file_name):
            print("The file does not exist")
            return

        target_dir = input("Enter the target directory: ")
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)

        shutil.move(file_name, target_dir)
        print(f"Moved {file_name} to {target_dir}")
    except Exception as e:
        print(f"An error occurred while moving the file: {e}")

def copy_file():
    try:
        file = input("Enter the file name you want to make a copy of: ")
        new_dir = input("Enter the new directory name: ")
        if not os.path.exists(file):
            print("The file does not exist")
            return
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        shutil.copy2(file, new_dir)  # copy the file to the new directory
    except Exception as e:
        print(f"An error occurred while copying the file: {e}")

def copy_directory(dir):
    try:
        new_dir = input("Enter the new directory name: ")
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        shutil.copytree(dir, new_dir)
    except Exception as e:
        print(f"An error occurred while copying the directory: {e}")

def remove_directory():
    try:
        f = input("Enter the file name you want to remove: ")
        if not os.path.exists(f):
            print("The file does not exist")
            return
        else:
            shutil.rmtree(f)
    except Exception as e:
        print(f"An error occurred while removing the directory: {e}")