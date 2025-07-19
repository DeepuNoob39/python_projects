import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter Rock/paper/scissors or Q to quit the game: ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_num = random.randint(0,2)
    computer_input = options[random_num]
    
    if user_input == "rock" and computer_input == "scissors":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_input == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_input == "paper":
        print("You won!")
        user_wins += 1
    
    else:
        print("You lost!")
        computer_wins += 1
        
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")

