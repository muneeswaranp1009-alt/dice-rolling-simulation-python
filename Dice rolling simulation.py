import random
import time

def print_dice(number):
    dice_faces = {
        1: ("\n |     |", " |  o  |", " |     |"),
        2: ("\n |o    |", " |     |", " |    o|"),
        3: ("\n |o    |", " |  o  |", " |    o|"),
        4: ("\n |o   o|", " |     |", " |o   o|"),
        5: ("\n |o   o|", " |  o  |", " |o   o|"),
        6: ("\n |o   o|", " |o   o|", " |o   o|")
    }
    
    for line in dice_faces[number]:
        print(line)

def start_game():
    print("=== Welcome to the Dice Simulator  ===")
    
    while True:
        input("\nPress ENTER to roll the dice...")
        print("Rolling...")
        time.sleep(0.5)
        
        result = random.randint(1, 6)
        
        print_dice(result)
        print(f"\nYou rolled a {result}!")
        
        # User kitta thirumba vilayada viruppama nu kekkurom
        choice = input("\nRoll again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thanks for playing! Goodbye")
            break

if __name__ == "__main__":
    start_game()