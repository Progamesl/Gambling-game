import random

def roll_dice():
    """Simulates rolling a dice and returns a random number between 1 and 6."""
    return random.randint(1, 6)

def main():
    print("Welcome to this Dice Gambling Game!")
    print("You have $100. Each round costs $10 to play.")
    print("If you guess the dice roll correctly, you win $50.")
    
    money = 100
    round_cost = 10
    winnings = 50
    
    while money >= round_cost:
        print(f"\nCurrent Balance: ${money}")
        bet = input("Enter your bet (1-6) or 'quit' to exit: ")
        
        if bet.lower() == 'quit':
            break
        
        try:
            bet_number = int(bet)
            if bet_number < 1 or bet_number > 6:
                print("Please enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
        
        money -= round_cost
        dice_result = roll_dice()
        print(f"The dice rolls: {dice_result}")
        
        if dice_result == bet_number:
            money += winnings
            print(f"Congratulations! You won ${winnings}.")
        else:
            print("Sorry, you lost this round.")
    
    print("\nGame Over. Made by Sid Shukla.")
    print(f"Final Balance: ${money}")

if __name__ == "__main__":
    main()
