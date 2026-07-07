#OOP Project #2 : Inventory & Item System

class Item:

    def __init__(self, name, item_type, value):

        self.name = name
        self.item_type = item_type
        self.value = value

    def display(self):

        print(f"Item Name: {self.name}")
        print(f"Item Type: {self.item_type}")
        print(f"Item Value: {self.value} Gold")

    def __str__(self):
        
        return f"{self.name} ({self.item_type}) - {self.value} Gold"

class Inventory:

    def __init__(self):

        self.items = []
    
    def add_item(self):

        item_name = input("Enter Name of New Item: ")
        item_type = input("Enter Item Type: ")
        item_value = int(input("Enter Item Value: "))

        item = Item(item_name, item_type, item_value)

        self.items.append(item)

        print("Item Successfully Added!")

    def remove_item(self):

        item_name = input("Enter the Name of the Item you wish to delete: ")
        
        for item in self.items:

            if item_name == item.name:

                self.items.remove(item)

                print("Item Successfully Removed!")

                return
        
        print("Item Not Found")

    def show_inventory(self):

        for item in self.items:

            print(item)

        if not self.items:

            print("Your Inventory is Empty.")

    def total_value(self):

        total = 0

        for item in self.items:

            total += item.value

        print(f"You have {total} Gold")

class Player:

    def __init__(self, name, hp, inventory):

        self.name = name
        self.hp = hp
        self.inventory = inventory

inventory = Inventory()
player = Player("Hero", 100, inventory)

while True: 

    print("===== Inventory =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show Inventory")
    print("4. Total Value")
    print("5. Exit")
    print("=====================")


    choice = input("Enter the Number of your Choosen Operation from the Menu: ")

    if choice == "1":

        player.inventory.add_item()

    elif choice == "2":

        player.inventory.remove_item()

    elif choice == "3":

        player.inventory.show_inventory()

    elif choice == "4":

        player.inventory.total_value()

    elif choice == "5":

        print("Thank You For Playing :D")

        break

    else:

        print("Plz Enter a Valid Number from the Game Menu.")