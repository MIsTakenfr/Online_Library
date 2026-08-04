import json

def main_menu():
    print(" Main Menu ".center(30, "="))
    print("\nPress 1. Books Menu")
    print("\nPress 2. Members Menu")
    print("\nPress 3. Exit")
    return input("\nPlease select main menu choice : ")

def add_to_json(file_name, list_name):
    with open(file_name, "w") as file:
        json.dump(list_name,file,indent=4)