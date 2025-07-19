print("Hello! Welcome to the game.")
ready = input("Do you want to play the quiz game? ")

if ready.lower() != "yes":
    quit()

print("Great! let's start")
score = 0

question1 = input("What's the capital of India? ").lower()
if question1 == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is New Delhi")
    
question2 = input("What's full form of RAM? ").lower()
if question2 == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is Random Access Memory")
    
question3 = input("What's the full form of CPU? ").lower()
if question3 == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is Central Processing Unit")
    
    
print(f"You got {score} questions correct.")
print(f"Your percentage is {score/3 * 100}%")
