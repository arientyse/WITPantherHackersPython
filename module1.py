import random

#import is a variable
#random is a library

number_of_guesses = 0
number_to_guess = random.randint(1,15)

#Use the pound sign to make comments

print("Please enter a number for me to guess!") #Print line
guess = int(input()) #Computer is going to do logic to guess the user's input
number_of_guesses += 1


#Control Flow: If, If...else, If...elif
#Loops keep programmers from having to write a statement multiple times

while guess != number_to_guess:

    if guess < number_to_guess:
        print("That's too low! Try again!")
        guess = int(input())
        number_of_guesses += 1

    if guess > number_to_guess:
        print("That's way too high! Try again!")
        guess = int(input())
        number_of_guesses += 1

    if guess == number_to_guess:
        print("YAY! You guessed the right answer!")
        print("Number of guesses is: " +str(number_of_guesses)) #How to use a varible in a string

        #This will be an endless loop without an exit condition
        #Concatnate - cannot add together

#Scope in programming is how you can access things



