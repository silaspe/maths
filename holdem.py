import random
import os

def pick_a_card():
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
    rank = random.choice(ranks)
    suit = random.choice(suits)
    return f"{rank} of {suit}!"

def deal_hand():
    return [pick_a_card(), pick_a_card()]

def deal_flop():
    return [pick_a_card() for _ in range(3)]

def deal_turn_or_river():
    return pick_a_card()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_confirmation(message="Press Enter when ready to proceed...", clear=True):
    input(message)
    if clear:
        clear_screen()

def texas_holdem():
    print("Welcome to Texas Hold 'Em!\n")

    # Player 1's turn
    input("Player 1, press Enter to receive your hand.")
    hand1 = deal_hand()
    clear_screen()
    print("Player 1's hand:")
    print("\n".join(hand1))
    wait_for_confirmation()

    # Player 2's turn
    input("Player 2, press Enter to receive your hand.")
    hand2 = deal_hand()
    clear_screen()
    print("Player 2's hand:")
    print("\n".join(hand2))
    wait_for_confirmation()

    # Dealing the Flop
    wait_for_confirmation("Press Enter to deal the flop.")
    flop = deal_flop()
    print("The Flop:")
    print("\n".join(flop))

    # Dealing the Turn
    wait_for_confirmation("Press Enter to deal the turn.", clear=False)
    turn = deal_turn_or_river()
    print("The Turn:")
    print(turn)

    # Dealing the River
    wait_for_confirmation("Press Enter to deal the river.", clear=False)
    river = deal_turn_or_river()
    print("The River:")
    print(river)

    print("All community cards have been dealt. The game continues!")

if __name__ == "__main__":
    texas_holdem()
