import os
import shutil
from functions import sort, move_file,remove_directory, copy_file, copy_directory,clear_desktop

def change_directory():
    dir = "/Users/Balog David/Desktop/da"
    while True:
        print("Current directory: ", dir)
        print()
        print("------------FILES------------")
        print()
        for k in os.listdir():
            print(k)
        print()
        print("-----------------------------")
        print()
        print("1. Sort the files in the current directory")
        print("2. Create a new directory")
        print("3. Rename a directory")
        print("4. Move a file to another directory")
        print("5. Copy a file to a directory")
        print("6. Copy the current directory to another directory")
        print("7. Remove a directory")
        print("0. Back")

        option = input("Enter the option: ")

        try:
            if option == '0':
                break
            elif option == '1':
                sort(dir)  # sort the files in the current directory
            elif option == '2':
                new_dir = input("Enter the directory name: ")
                os.mkdir(new_dir)  # create the new directory
            elif option == '3':
                new_dir = input("Enter the directory name: ")
                os.rename(dir, new_dir)  # rename the directory
                dir = new_dir
            elif option == '4':
                move_file()
            elif option == '5':
                copy_file()
            elif option == '6':
                copy_directory(dir)
            elif option == '7':
                remove_directory()
            else:
                print("Invalid option")
                continue
        except Exception as e:
            print(f"An error occurred: {e}")


def navigate_directory():
    dir = "/Users/Balog David/Desktop/da"
    while True:
        for file in os.listdir():
            print(file)

        new_dir = input("Enter the directory name you want to go next or 'main' to go to the main menu or 'back' to go to the previous directory: ")

        try:
            if new_dir == 'main':
                break
            if new_dir == 'back':
                dir = os.path.dirname(dir)  # go to the previous directory
                os.chdir(dir)
            if not os.path.exists(new_dir):
                print("The directory does not exist")
                continue
            else:
                dir = os.path.join(dir, new_dir)
                os.chdir(dir)
        except Exception as e:
            print(f"An error occurred: {e}")


def run():
    os.chdir('/Users/Balog David/Desktop/da')
    while True:
        for file in os.listdir():
            print(file)
        print("1. Change the current directory")
        print("2. Navigate to another directory")
        print("3. Clear the desktop")
        print("0. Exit")
        option = input("Enter the option: ")
        if option == '0':
            break
        elif option == '1':
            change_directory()
        elif option == '2':
            navigate_directory()
        elif option == '3':
            clear_desktop()
        else:
            print("Invalid option")
            continue
