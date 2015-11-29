from random import randint

#Game_play function: ask first question and check if it is correct or not
def start_quiz(quiz, blanks, answers):
	print quiz
	for quiz_num in range(0, len(blanks)):
		user_input= raw_input ("What's " + blanks[quiz_num] + "? ")
		while user_input != answers[quiz_num]:
			user_input= raw_input ("oohoh.. incorrect. Try again. What's " + blanks[quiz_num] + "? ")
		quiz = quiz.replace(blanks[quiz_num], answers[quiz_num])
		print quiz
		if quiz_num == 3: #need to make 3 more understandable
			print "Congratulations! You finished the quiz."

# Easy quiz
# Quiz title and complete lyrics as answer
title = "Itsy-Bitsy Spider"
lyrics = "The itsy-bitsy spider climbed up the water spout. Down came the rain and washed the spider out. Out came the sun and dried up all the rain. And the itsy-bitsy spider climbed up the spout again"

# Easy Quiz itself
easy_quiz = "The itsy-bitsy _1____ climbed up the water _2___. Down came the _3__ and washed the spider out. Out came the _4__ and dried up all the rain. And the itsy-bitsy spider climbed up the spout again"

# A list of blank numbers to be passed into the start_quiz function
parts_of_lyrics_easy  = ["_1____", "_2___", "_3__", "_4__"]

# Correct answers for easy quiz
correct_answers_easy = ["spider", "spout", "rain", "sun"]

# try function start_quiz
start_quiz(easy_quiz, parts_of_lyrics_easy, correct_answers_easy)

