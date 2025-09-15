import random

print("Welcome to the Rock, Paper and Scissors game!")
print("Rules are simple, whoever have the most wins out of 3 is the overall winner.")
print("Write 'r' for Rock\nWrite 'p' for Paper\nWrite 's' for scissors")
emojis = {
    "r": "\u270A",
    "p": "\u270B",
    "s": "\u270C"
    
}

user_win_count = 0
tie_count = 0
comp_win_count = 0
count = 0

while True:
    count += 1
    user_input = input("Choose from Rock, Paper, Scissor (r, p, or s): ").lower().strip()
    comp_input = random.choice(["r", "s", "p"])

    if user_input == "r":
        print(f"You chose {emojis[user_input]}")
        if comp_input == "r":
            print(f"Computer chose {emojis[comp_input]}")
            print("It's a tie!")
            tie_count += 1
        
        elif comp_input == "p":
            print(f"Computer chose {emojis[comp_input]}")
            print("You lose!")
            comp_win_count += 1
        
        elif comp_input == "s":
            print(f"Computer chose {emojis[comp_input]}")
            print("You win!")
            user_win_count += 1
            
    elif user_input == "p":
        print(f"You chose {emojis[user_input]}")
        if comp_input == "r":
            print(f"Computer chose {emojis[comp_input]}")
            print("You win!")
            user_win_count += 1
        
        elif comp_input == "p":
            print(f"Computer chose {emojis[comp_input]}")
            print("It's a tie!")
            tie_count += 1
        
        elif comp_input == "s":
            print(f"Computer chose {emojis[comp_input]}")
            print("You lose!")
            comp_win_count += 1
            
    elif user_input == "s":
        print(f"You chose {emojis[user_input]}")
        if comp_input == "r":
            print(f"Computer chose {emojis[comp_input]}")
            print("You lose!")
            comp_win_count += 1
        
        elif comp_input == "p":
            print(f"Computer chose {emojis[comp_input]}")
            print("You win!")
            user_win_count += 1
        
        elif comp_input == "s":
            print(f"Computer chose {emojis[comp_input]}")
            print("It's a tie!")
            tie_count += 1
    
    else:
        print("Please enter a valid input.")
        continue
    
    if count == 3:
        break
    # permission = input("Do you want to continue? Yes or No (y/n) ").lower().strip()
    # if permission == "n":
    #     break

print(f"Your wins = {user_win_count}\nComupter wins = {comp_win_count}\nTies = {tie_count}")

if user_win_count >= 2:
    print(f"Overall winner is You")

else:
    print(f"Overall winner is Computer")


print("Thanks for playing the game! Come again next time")

