import json
import string
import requests

start_url = 'http://jswidler.com/challenge'
# expects a url params 
# {
# 	'solverName': <string>
# }

# returns a response like 
#
# {
#     "challengeId": 2594,
#     "token": "vqf851wn5whtttjz8oom",
#     "startingSecretLength": 2,
#     "allowedGuesses": 5000,
#     "guessUrl": "http://jswidler.com/challenge/guess"
# }

guess_url = 'http://jswidler.com/challenge/guess'
# expects url params
# {
# 	'token': <from start_url>,
# 	'guess': 'aa'
# }

# returns
# {
# 	  "token": "qkjacwryu8w0ri5mj30h",
# 	  "message": "The last guess had 0 out of 2 letters correct.",
# 	  "numberLettersCorrect": 0,
# 	  "level": 1,
# 	  "secretLength": 2,
# 	  "guessesLeft": 4999
# }

solver_name = 'jzebra_naive_00'
# setting these as global variables to make things easier. 
# pass these as params to guess() when we want to clean it up.
token = None
secret_length = None
last_guess = None

def start_game():
	params = {
		'solverName': solver_name
	}

	response = requests.post(start_url, params=params)
	global token
	global secret_length
	token = str(response.json().get('token'))
	secret_length = int(response.json().get('startingSecretLength')) 

def run():
	start_game()
	print token
	print secret_length

# part 1: building the score map for each position
# treat each letter in the guess as a separate problem
# change the letter
# concat many letters to make a guess
# submit the new guess
# each position in the guess has a letter: score map. if numberLettersCorrect increases, increment the score 
# repeat changing the letter until we reach z OR the total numberLettersCorrect for this level == secretLength
# 
# part 2: guessing from the map
# using the highest scoring letters for each position, make a guess
# change one position
# if score decreases, undo the change
# if score increases, lock in the change
# else, repeat



if __name__ == "__main__":
	run()