#!/usr/bin/python
import sys
from random import randint

#Welcome page
print "Welcome to number-guess.py!  The goal of this game \n\
is to guess the number that the game generates."

#Difficulty choice
print "What difficuly level would you like to play?"
difficuly = raw_input("Do you want to be (A) begginner,\
(B) intermediate or (C) advanced? ")
if difficuly == "A":
    remaining_guesses = 30
elif difficuly == "B":
    remaining_guesses = 20
elif difficuly == "C":
	remaining_guesses = 10
else :
    print "unkown option..setting to easy"

#Random number selection
number_to_guess = randint(0,100)

#ask user for guesses
#set winner to false for the while loop
winner = False
while winner is not True:
	#ask user for their input, store as int
	guess = int(raw_input('Guess a number between 0 and 100: '))
	if guess == number_to_guess:
		#This will exit the while loop
		winner = True
	elif guess != number_to_guess:
		#Hin the user for gt or le
		if guess > number_to_guess:
			print "your guess is too high"
		elif guess < number_to_guess:
			print "your guess is too low"
		#counter..it hits 0 and user loses
		remaining_guesses = remaining_guesses - 1
		print "You have %s guesses left" % (remaining_guesses)
		#exit clause for when guesses hit 0
		if remaining_guesses <= 1:
			print "you ran out of guesses...fail"
			sys.exit()
print "Winner!"