# No difficulty this time jus the plain logic of the game
# Random choice for who will draw first
import random

user_choice = input("Who'll draw first, type me or opponent: ").lower()

match user_choice:
    case "me":
        pass
    case "opponent":
        pass

values = {
    "Ace": 11,
    "2":  2,
    "3":  3,
    "4":  4,
    "5":  5,
    "6":  6,
    "7":  7,
    "8":  8,
    "9":  9,
    "10": 10,
    "King": 10,
    "Queen": 10,
    "Jack": 10,
}

print(values["Ace"])