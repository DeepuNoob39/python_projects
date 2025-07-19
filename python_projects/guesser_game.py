import random

range_of_number = input("Enter a number: ")

if range_of_number.isdigit():
    range_of_number = int(range_of_number)
else:
    print("Wrong Input! Enter a number next time.")
    quit()

random_number = random.randint(0, range_of_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Wrong input!")
        quit()
        
    if user_guess == random_number:
        print("You got it!")
        break
        
    elif user_guess > random_number:
        print("Your guess was higher!")
    
    elif user_guess < random_number:
        print("Your guess was lower!")
        
        
print("You guessed the number in", guesses, "times")
