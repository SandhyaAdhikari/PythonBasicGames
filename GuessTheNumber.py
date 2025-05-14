import random

secret_number= random.randint(1,100)
attempts=0

print("Are You Ready To Play Guess The number?")
print("To get started, think of a number between 1 to 100.")

while True:
    guess= input("take a guess: ") #takes input from the user, and the string is the prompt shown to the user

    if not guess.isdigit(): #checks if i/p consists of only digits
        print("please enter a valid number:")
        continue

    guess= int(guess) # converts the guess from string to integer
    attempts+=1

    if guess<secret_number:
        print("too low")
    elif guess>secret_number:
        print("too high")
    else:
        print(F"yippie! thats correct. you guessed it in {attempts} tries yayyayay")#f is used for formatted string and replace attempts with variable value
        break
