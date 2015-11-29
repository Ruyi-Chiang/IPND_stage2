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
		if quiz_num == len(blanks) - 1: #need to make 3 more understandable
			print "Congratulations! You finished the quiz."

# Easy quiz
# Quiz title and complete lyrics as answer
easy_quiz_title = "Itsy-Bitsy Spider"
lyrics_easy = "The itsy-bitsy spider climbed up the water spout. Down came the rain and washed the spider out. Out came the sun and dried up all the rain. And the itsy-bitsy spider climbed up the spout again"

# Easy Quiz itself
easy_quiz = "The itsy-bitsy _1____ climbed up the water _2___. Down came the _3__ and washed the spider out. Out came the _4__ and dried up all the rain. And the itsy-bitsy spider climbed up the spout again"

# A list of blank numbers to be passed into the start_quiz function
parts_of_lyrics_easy  = ["_1____", "_2___", "_3__", "_4__"]

# Correct answers for easy quiz
correct_answers_easy = ["spider", "spout", "rain", "sun"]

# try function start_quiz
start_quiz(easy_quiz, parts_of_lyrics_easy, correct_answers_easy)

#Medium quiz
medium_quiz_title = "Let it go"
lyrics_medium = "Don't let them in, don't let them see. Be the good girl you always have to be. Conceal, don't feel, don't let them know. Well now they know.  Let it go, let it go. Can't hold it back anymore. Let it go, let it go. Turn away and slam the door. I don't care what they're going to say. Let the storm rage on. The cold never bothered me anyway"

medium_quiz = "Don't let them in, don't let them see. Be the good _1__ you always have to be. Conceal, don't feel, don't let them know. Well now they know.  Let it go, let it go. Can't hold it back _2_____. Let it go, let it go. Turn away and slam the door. I don't _3__ what they're going to say. Let the _4___ rage on. The cold never bothered me _5____"

parts_of_lyrics_medium  = ["_1__", "_2_____", "_3__", "_4___", "_5____"]

correct_answers_medium = ["girl", "anymore", "care", "storm", "anyway"]

start_quiz(medium_quiz, parts_of_lyrics_medium, correct_answers_medium)






# Hard quiz
hard_quiz_title = "Hello"
lyrics_hard = "Hello, it's me. I was wondering if after all these years you'd like to meet. To go over everything. They say that time's supposed to heal ya. But I ain't done much healing. Hello, can you hear me. I'm in California dreaming about who we used to be. When we were younger and free. I've forgotten how it felt before the world fell at our feet"

hard_quiz = "Hello, it's _1. I was _2_______ if after all these years you'd like to meet. To go over everything. They say that time's supposed to heal ya. But I ain't done much _3_____. Hello, can you _4__ me. I'm in _5________ dreaming about who we used to be. When we were _6_____ and free. I've forgotten how it felt before the world fell at our feet"

parts_of_lyrics_hard  = ["_1", "_2_______", "_3_____", "_4__", "_5________", "_6_____"]

correct_answers_hard = ["me", "wondering", "healing", "hear", "California", "younger"]

start_quiz(hard_quiz, parts_of_lyrics_hard, correct_answers_hard)
