import random


def CreateDeck():
    deck = {
        "Bulbasaur": {"Strength": 64, "Agility": 48, "Defence": 38, "Attack": 77},
        "Charmander": {"Strength": 60, "Agility": 65, "Defence": 43, "Attack": 80},
        "Squirtle": {"Strength": 58, "Agility": 43, "Defence": 65, "Attack": 50},
        "Caterpie": {"Strength": 30, "Agility": 45, "Defence": 35, "Attack": 20},
        "Weedle": {"Strength": 35, "Agility": 50, "Defence": 40, "Attack": 25},
        "Pidgey": {"Strength": 55, "Agility": 72, "Defence": 46, "Attack": 32},
    }
    return deck


def DrawCard(deck):
    return random.choice(list(deck.keys()))


def ShowCard(deck, card):
    print(card + ": " + str(deck[card]))


def player_choice(deck, card):
    print("\nYour card is " + card)
    ShowCard(deck, card)

    print("\nChoose a stat:")
    print("1 - Strength")
    print("2 - Agility")
    print("3 - Defence")
    print("4 - Attack")

    choice = int(input("Enter number: "))

    if choice == 1:
        return deck[card]["Strength"]
    elif choice == 2:
        return deck[card]["Agility"]
    elif choice == 3:
        return deck[card]["Defence"]
    elif choice == 4:
        return deck[card]["Attack"]
    else:
        print("Invalid entry")
        return None


def CompareCards(deck):
    player_card = DrawCard(deck)
    computer_card = DrawCard(deck)

    print("\nYou drew:")
    ShowCard(deck, player_card)

    print("\nComputer drew:")
    ShowCard(deck, computer_card)

    player_stat = player_choice(deck, player_card)

    stat_list = ["Strength", "Agility", "Defence", "Attack"]
    stat_name = random.choice(stat_list)
    computer_stat = deck[computer_card][stat_name]

    print("\nComputer chose: " + stat_name)
    print("Your stat: " + str(player_stat))
    print("Computer stat: " + str(computer_stat))

    if player_stat is None:
        return

    if player_stat > computer_stat:
        print("You win!")
    elif player_stat < computer_stat:
        print("Computer wins!")
    else:
        print("It is a tie!")


deck = CreateDeck()
CompareCards(deck)
