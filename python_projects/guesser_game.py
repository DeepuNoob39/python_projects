import random

print("Welcome to the Guesser Game.\nRule is simple- computer will choose a number and you will have to guess it.")
range_of_secret_num = int(input("What should be the highest range of the secret number? "))
secret_num = random.randint(1, range_of_secret_num)
count = 0

while True:
    try:
        user_guess = int(input(f"Guess the number between 1 and {range_of_secret_num} : "))
    except ValueError:
        print("Please enter the valid number.")
        continue
    if user_guess < secret_num:
        print("Your guess was too low, try again.")
        count += 1
        continue
    
    elif user_guess > secret_num:
        print("Your guess was too high, try again.")
        count += 1
        continue
    
    else:
        print("Congrats! you guessed it right.")
        count += 1
        print(f"It took you {count} times to guess the number.")
        break
    
        
    
    
#should give hints like too low or too high
#on correct guess, give thanks and no of counts it took
