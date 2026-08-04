import random 

def CreateDeck():
    deck = {
        
        "Bulbasaur": {"Strength": 64, "Agility": 48, "Defence": 38,"Attack": 77},
        "Charmander": {"Strength": 64, "Agility": 48, "Defence": 38,"Attack": 77},
        "Squirtle": {"Strength": 64, "Agility": 48, "Defence": 38,"Attack": 77},
        "Catapie": {"Strength": 64, "Agility": 48, "Defence": 38,"Attack": 77},
        "Weedle": {"Strength": 64, "Agility": 48, "Defence": 38,"Attack": 77},
        "Pidgey": {"Strength": 55, "Agility": 72, "Defence": 46,"Attack":32},
    }
    return deck

def DrawCard():
    global card
    card = random.choice(list(CreateDeck().keys()))
    return card
    
def LabelCard():
    return CreateDeck()[card]
 

def ShowCard():
    print(DrawCard())
    print(LabelCard())
    
def player_choice():
    print("\nChoose a stat:")
    print("1 - Strength")
    print("2 - Agility")
    print("3 - Defence")
    print("4 - Attack")

        
    choice = int(input("Enter number: "))
        
    if choice == 1:
        stat = CreateDeck()[card]["Strength"]
    elif choice == 2:
        stat = CreateDeck()[card]["Agility"]
    elif choice == 3:
        stat = CreateDeck()[card]["Defence"]
    elif choice == 4:
        stat = CreateDeck()[card]["Attack"]
    else:
        print("Invalid Entry")
        return 0
    return stat


def CompareCards():
    DrawCard()
    player_choice()
    


#UpdateScore()

CreateDeck()

DrawCard()

ShowCard()

print(player_choice())