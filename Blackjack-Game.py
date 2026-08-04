import random


# --- HIGH SCORE SYSTEM (ADDED) ---
def LoadHighScore():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except:
        return 0


def SaveHighScore(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))


def CreateDeck():
    return {
        "Bulbasaur": {"Strength": 64, "Agility": 48, "Defence": 38, "Attack": 77},
        "Charmander": {"Strength": 60, "Agility": 65, "Defence": 43, "Attack": 80},
        "Squirtle": {"Strength": 58, "Agility": 43, "Defence": 65, "Attack": 50},
        "Caterpie": {"Strength": 30, "Agility": 45, "Defence": 35, "Attack": 20},
        "Weedle": {"Strength": 35, "Agility": 50, "Defence": 40, "Attack": 25},
        "Pidgey": {"Strength": 55, "Agility": 72, "Defence": 46, "Attack": 32},
    }


def DrawCard(deck):
    return random.choice(list(deck.keys()))


def ShowCard(deck, card):
    print(card + ": " + str(deck[card]))


def get_int_input(prompt, min_value=None):
    while True:
        user_input = input(prompt)

        try:
            value = int(user_input)
            if min_value is not None and value < min_value:
                print("Please enter a number >= " + str(min_value))
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a number.")


def get_choice():
    print("\nChoose a stat:")
    print("1 - Strength")
    print("2 - Agility")
    print("3 - Defence")
    print("4 - Attack")

    while True:
        choice = get_int_input("Enter number: ")
        if choice in [1, 2, 3, 4]:
            return choice
        print("Invalid choice. Pick 1 to 4.")


def get_stat_name(choice):
    if choice == 1:
        return "Strength"
    if choice == 2:
        return "Agility"
    if choice == 3:
        return "Defence"
    if choice == 4:
        return "Attack"
    return "Strength"


def PlayRound(deck):
    player_card = DrawCard(deck)
    computer_card = DrawCard(deck)

    print("\nYou drew:")
    ShowCard(deck, player_card)

    print("\nComputer drew:")
    ShowCard(deck, computer_card)

    choice = get_choice()
    stat_name = get_stat_name(choice)

    player_stat = deck[player_card][stat_name]
    computer_stat = deck[computer_card][stat_name]

    print("\nStat chosen: " + stat_name)
    print("Your stat: " + str(player_stat))
    print("Computer stat: " + str(computer_stat))

    if player_stat > computer_stat:
        print("You win this round!")
        return 1, 0
    elif player_stat < computer_stat:
        print("Computer wins this round!")
        return 0, 1
    else:
        print("It is a tie!")
        return 0, 0


def ask_play_again():
    while True:
        answer = input("\nPlay again? (y/n): ").lower()
        if answer == "y" or answer == "n":
            return answer
        print("Please enter y or n.")


def Game():
    deck = CreateDeck()

    # --- HIGH SCORE LOAD (ADDED) ---
    high_score = LoadHighScore()
    print("Current High Score: " + str(high_score))

    while True:
        player_score = 0
        computer_score = 0

        rounds = get_int_input("How many rounds? ", 1)

        for i in range(rounds):
            print("\n--- Round " + str(i + 1) + " ---")
            p, c = PlayRound(deck)
            player_score += p
            computer_score += c

            print("\nScore:")
            print("Player: " + str(player_score))
            print("Computer: " + str(computer_score))

        print("\nFinal Score:")
        print("Player: " + str(player_score))
        print("Computer: " + str(computer_score))

        # --- HIGH SCORE CHECK (ADDED) ---
        if player_score > high_score:
            high_score = player_score
            SaveHighScore(high_score)
            print("New High Score: " + str(high_score))
        else:
            print("High Score: " + str(high_score))

        if player_score > computer_score:
            print("You won the game!")
        elif player_score < computer_score:
            print("Computer won the game!")
        else:
            print("The game is a tie!")

        if ask_play_again() == "n":
            break


Game()