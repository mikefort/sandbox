#!/usr/bin/python
import sys
from random import randint
import shelve
import argparse

#Flag --highscores to just see the high scores. Optional
parser = argparse.ArgumentParser(description ='For first time users,\
	please run clear arg to itiate the database(shelve)')
parser.add_argument('--highscores', action='store_true'\
	, help='high scores print')
parser.add_argument('--clear', action='store_true', \
	help='clear scores and initiate new shelve')

args = parser.parse_args()

#If this is flagged it will print high scores and exit
if args.highscores:
	d = shelve.open('highschores.db')
	high_score_advanced = d['high_score_advanced']
	high_score_intermediate = d['high_score_intermediate']
	high_score_begginner = d['high_score_begginner']
	high_score_advanced_name = d['high_score_advanced_name']
	high_score_intermediate_name = d['high_score_intermediate_name']
	high_score_begginner_name = d['high_score_begginner_name']
	print "Current high scores (# of guesses left) : "
	print "Advanced - %s - %s" %(high_score_advanced, high_score_advanced_name)
	print "Intermediate - %s - %s" %(high_score_intermediate, high_score_intermediate_name)
	print "Beginner - %s - %s" %(high_score_begginner, high_score_begginner_name)
	sys.exit()

if args.clear:
	print "clearing scores..."
	d = shelve.open('highschores.db')
	d['high_score_begginner'] = 0
	d['high_score_begginner_name'] = ""
	d['high_score_intermediate'] = 0
	d['high_score_intermediate_name'] = ""
	d['high_score_advanced'] = 0
	d['high_score_advanced_name'] = ""
	print "cleared.."
	sys.exit()
'''
Begin Game Code Here:
'''

#Open shelve with high score information
d = shelve.open('highschores.db')
high_score_advanced = d['high_score_advanced']
high_score_intermediate = d['high_score_intermediate']
high_score_begginner = d['high_score_begginner']
high_score_advanced_name = d['high_score_advanced_name']
high_score_intermediate_name = d['high_score_intermediate_name']
high_score_begginner_name = d['high_score_begginner_name']

#Welcome page
print "The goal of this game \
is to guess the number that the game generates. \
The number generated is between 0 and 1000.\nYou get a number of \
guesses based on the difficulty setting chosen.\n\
The quicker you guess \
correctly the higher the score!"
print "Current high scores (# of guesses left) : "
print "Advanced - %s - %s" %(high_score_advanced, high_score_advanced_name)
print "Intermediate - %s - %s" %(high_score_intermediate, high_score_intermediate_name)
print "Beginner - %s - %s" %(high_score_begginner, high_score_begginner_name)

#Difficulty choice selection
#We set number of guesses for each difficulty as well as interger range
print "What difficuly level would you like to play?"
difficuly = raw_input("Do you want to be \n(A) begginner(25 guesses)\n\
(B) intermediate(20 guesses)\n(C) advanced(15 guesses)\n \n")

if difficuly == "A":
	number_to_guess = randint(0,100)
	remaining_guesses = 15
elif difficuly == "B":
	number_to_guess = randint(0,5000)
	remaining_guesses = 15
elif difficuly == "C":
	remaining_guesses = 15
	number_to_guess = randint(0,1000)
else :
    print "unkown option..setting to easy"
    remaining_guesses = 30
    difficuly = "A"

#ask user for guesses
#set winner to false for the while loop
winner = False
while winner is not True:
	#ask user for their input, store as int
	guess = int(raw_input('Guess the number generated: ')) 
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
#Winning sequence
print "Winner!"
if difficuly == "A":
    if remaining_guesses >= high_score_begginner:
    	print "High score!"
    	high_score_begginer_name = raw_input('your name please: ')
    	d['high_score_begginner'] = remaining_guesses
    	d['high_score_begginner_name'] = high_score_begginer_name
elif difficuly == "B":
	if remaining_guesses >= high_score_intermediate:
		print "High score!"
    	high_score_intermediate_name = raw_input('your name please: ')
    	d['high_score_intermediate'] = remaining_guesses
    	d['high_score_intermediate_name'] = high_score_intermediate_name
elif difficuly == "C":
	if remaining_guesses >= high_score_advanced:
		print "High score!"
    	high_score_advanced_name = raw_input('your name please: ')
    	d['high_score_advanced'] = remaining_guesses
    	d['high_score_advanced_name'] = high_score_advanced_name