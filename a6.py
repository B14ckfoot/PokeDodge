import random

def computerChoice():
    listChoices = ["rock", "paper", "scissors"]
    return random.choice(listChoices)
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
def print_score(player_score, computer_score):
    print(f"Your score: {player_score}  Computer score: {computer_score}")
def main():
    player_score = 0
    computer_score = 0
    rounds_played = 0

    while rounds_played < 3:
        player_choice = input("Enter your choice (rock, paper, scissors), or 'quit' to end the game: ").lower()
        if player_choice == "quit":
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = computerChoice()
        print(f"Computer chooses: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        print(winner)

        if winner == "You win!":
            player_score += 1
        elif winner == "Computer wins!":
            computer_score += 1

        rounds_played += 1
        print_score(player_score, computer_score)

    if player_score > computer_score:
        print("Congratulations! You win the game!")
    elif player_score < computer_score:
        print("Sorry, Computer wins the game!")
    else:
        print("It's a tie!")

    print("Thanks for playing!")
main()