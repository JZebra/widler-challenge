import json
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

solverName = 'jzebra_00'
# setting these as global variables to make things easier. 
# pass these as params to guess() when we want to clean it up.
token = None
secretLength = None

def start_game():
	params = {
		'solverName': solverName
	}

	response = requests..post(start_url, params=params)
	global token
	global secretLength
	token = str(response.get('token'))
	secretLength = int(response.get('secretLength'))

def guess():



def run():
