#!/usr/bin/env python3

# CITC-2391 Summer 2020
# Wizard Inventory
# Name: Caleb Brown
# Date: 07/23/2020


def display_menu():  # This function displays the menu commands
    print("COMMAND MENU")
    print("show - Show All Items")
    print("add - Add an Item")
    print("change - Change an Item")
    print("drop - Drop and Item")
    print("exit - Exit Program")
    print()


def show_inventory(inventory):  # Shows the inventory using a for loop.
    i = 1
    for item in inventory:
        print(str(i) + " - " + item)
        i += 1  # i increments to show the numbers before the inventory item.
    print()


def add_to_inventory(inventory):  # Adds and item to the inventory using append()
    wizard_item = input("Name: ")
    inventory.append(wizard_item.lower())
    i = inventory.index(wizard_item)  # added this in so I could use the index function. Finds the index of the item.
    print(wizard_item + " was added as item number " + str(i + 1) + ".")  # Added 1 to i since the list starts at 0.
    print()


def change_item(inventory):  # This function changes an item in the inventory
    item_number = int(input("Item Number: ")) - 1  # Subtracted 1 from the user given number.
    if item_number < 1 or item_number > len(inventory):
        print("Item not found.")
        print()
    else:
        index_item = inventory[item_number]
        inventory.remove(index_item)  # This drops the item.
        item_name = input("Updated Name: ")
        inventory.insert(item_number, item_name.lower())  # This inserts the item at the specified index.
        print("Item Number " + str(item_number + 1) + " was updated.")  # Added 1 back for the output.
        print()


def drop_item(inventory):  # Drops an item from the inventory.
    item_number = int(input("Item Number: "))
    if item_number < 1 or item_number > len(inventory):
        print("Item not found.")
        print()
    else:
        dropped_item = inventory.pop(item_number - 1)  # Assigned the dropped item to a variable for later use.
        print(dropped_item + " was dropped.")  # Later use of the dropped_item variable.
        print()


def main():  # Main function
    inventory = ["wooden staff", "wizard hat", "cloth shoes"]  # Inventory list
    print("The Wizard Inventory Program")
    print()
    display_menu()  # calls the menu
    while True:
        command = input("Command: ")
        if command.lower() == "show":
            show_inventory(inventory)  # shows the inventory
        elif command.lower() == "add":
            add_to_inventory(inventory)  # adds to the inventory
        elif command.lower() == "change":
            change_item(inventory)  # changes an item in the inventory
        elif command.lower() == "drop":
            drop_item(inventory)  # drops an item in inventory
        elif command.lower() == "exit":  # Exits the program.
            print("Bye!")
            break
        else:  # Gives an error if the command is invalid
            print("Invalid Command")
            print()
            continue  # continues the loop.


if __name__ == '__main__':
    main()
