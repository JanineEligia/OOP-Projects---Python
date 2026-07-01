# OOP Project #1 : RPG Character Manager

class Player:

    def __init__(self, name, hp, attack, defense, level):
        
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.level = level
    
    def display_stats(self):

        print(f"Name: {self.name} lvl. {self.level}")
        print(f"Stats: HP: {self.hp}, ATK: {self.attack}, DEF: {self.defense}")
         
    def take_damage(self, amount):

        self.hp -= amount

        if self.hp <= 0:
    
            self.hp = 0
            print(f"{self.name} took {amount} damage.")
            print(f"{self.name} now has {self.hp} hp.")
            print(f"{self.name} has died.")

        elif self.hp > 0:

            print(f"{self.name} took {amount} damage.")
            print(f"{self.name} now has {self.hp} hp.")

    def heal(self, amount):

        self.hp += amount
        print(f"{self.name} has gained {amount} hp.")
        print(f"{self.name} now has {self.hp} hp.")

    def level_up(self):

        print(f"{self.name} has now leveled up!")
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.defense += 3
        print(f"Name: {self.name} lvl. {self.level}")
        print(f"Stats: HP: {self.hp}, ATK: {self.attack}, DEF: {self.defense}")

player = None

while True:

    print("===== RPG Character Manager =====")
    print("1. Create Character")
    print("2. Show Character")
    print("3. Attack Character")
    print("4. Heal Character")
    print("5. Level Up")
    print("6. Exit")
    print("=================================")

    choice = input("What would you like to do? (Type in Number of your choosen task): ")

    if choice == "1":
        
        name = input("Enter Name: ")
        hp = 100
        attack = 50
        defense = 25
        level = 1

        player = Player(name, hp, attack, defense, level)

    elif choice == "2":

        if player is None:

            print("Please create a character first!")

        else:

            player.display_stats()

    elif choice == "3":

        if player is None:

            print("Please create a character first!")

        else:

            damage = int(input("How much damage do you want to inflict?: "))
            player.take_damage(damage)

    elif choice == "4":

        if player is None:

            print("Please create a character first!")

        else:

            heal = int(input("How much HP do you want to heal? "))
            player.heal(heal)

    elif choice == "5":

        if player is None:

            print("Please create a character first!")

        else: 

            player.level_up()

    elif choice == "6":

        print("Thank you for playing <3")
        break

    else: 

        print("Plz select a valid number from the menu provided. ")


