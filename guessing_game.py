# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anthony Guzman
# Assignment: guessing_game
# Date:  09 November 2022

import random
#the following function will simply explain the game when called
def header():
    print('Guess the secret number between 1 and 100!: ')

#the following function is how the guessing game actually works
def guessloop(guess,randomNum,count):
    while guess != randomNum: #if the number guessed by the user is not the same as the randomNum then the following loop will occur
        try:
            guess = int(input('Input Guess: '))

            if guess > randomNum: #if the number inputed is larger than the number being guessed, the user must input a new guess
                count += 1
                print('Your guess is too high! Try Again: ')
                continue #continues the loop

            elif guess < randomNum: #if number guessed is too small the user must guess again
                count += 1
                print('Your guess is too low! Try Again: ')
                continue

            if guess == randomNum: #if the guess is correct a message is diplayed and the game is over
                count += 1
                print(f'You guessed it! The correct answer was {randomNum}, it took you {count} guesses')
                continue

        except: #if nothing under is valid, the following exception will occurr
            count += 1
            print('Bad input, Try Again: ')
            continue

def guessing(): # here we call on the previous two functions aswell as create new variables
    header()
    secretNum = random.randint(1,100) #the number the user is trying to guess
    guess = -1 #the number the user has inputted, I have it set to -1 (arbitrary number it just needed to not be 26)
    count = 0 #the amount of guesses starts at 0 and is updated as the user inputs guesses
    guessloop(guess,secretNum,count)

guessing() #guessing() is called and the code starts

input('Press Enter to close')