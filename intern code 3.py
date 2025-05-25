import random

def get_user_choice():
    while True:
        choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid input. Please choose Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("=================================")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("Result: It's a tie!")
        elif winner == "user":
            print("Result: You win this round!")
            user_score += 1
        else:
            print("Result: Computer wins this round!")
            computer_score += 1

        print(f"\nScores => You: {user_score} | Computer: {computer_score}\n")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            print(f"Final Scores => You: {user_score} | Computer: {computer_score}")
            break
        print("----------------------------------")

# Run the game
play_game()
