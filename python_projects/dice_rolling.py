import random
import sys

print("Welcome to the Dice Rolling game!")
count = 0

try:
    no_of_times = int(input("How many times do you want to roll the dice? "))
except ValueError:
    print("Invalid input, please give integer value.")
    sys.exit()
    
while no_of_times:
    user_input = input("Do you want to roll the dice?(y/n) ").lower().strip()
    if user_input == "y":
        first_result = random.randint(1,6)
        second_result = random.randint(1,6)
        print(f"({first_result}, {second_result})")
        no_of_times -= 1
        count = count + 1
    
    elif user_input == "n" or user_input == "N":
        break
    
    else:
        print("Invalid input, try again.")

if no_of_times == 0:
    print(
        f"""Thanks for playing the game!
You rolled the dice for {count} times. Come back again next time.
        """)
    