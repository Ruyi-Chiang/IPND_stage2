from random import randint

# Quiz title and complete lyrics as answer
title = "Itsy-Bitsy Spider"
lyrics = "The itsy-bitsy spider climbed up the water spout. Down came the rain and washed the spider out. Out came the sun and dried up all the rain. And the itsy-bitsy spider climbed up the spout again"

# Quiz
quiz = "The itsy-bitsy _1____ climbed up the water _2___. Down came the _3__ and washed the spider out. Out came the _4__ and dried up all the rain. And the itsy-bitsy spider climbed up the spout again"
print quiz

# A list of replacement words to be passed in to the play game function. 
parts_of_speech1  = ["_1____", "_2___", "_3__", "_4__"]

# Correct answers
correct_answers = ["spider", "spout", "rain", "sun"]


#Ask first question and check if it is correct or not
user_input= raw_input ("What's " + parts_of_speech1[0] + "? ")
while user_input != correct_answers[0]:
	user_input= raw_input ("oohoh.. incorrect. Try again. What's " + parts_of_speech1[0] + "? ")
quiz = quiz.replace(parts_of_speech1[0], correct_answers[0])
print quiz
	


# Ask for user's input for 4 questions and save them into a list
# answers = []
# for question in parts_of_speech1:
# 	user_input= raw_input ("What's " + question + "? ")
# 	answers.append(user_input)
# print answers



# quiz = quiz.replace("_1____", first_replacement)
# quiz = quiz.replace("_2___", second_replacement)
# quiz = quiz.replace("_3__", third_replacement)
# quiz = quiz.replace("_4__", forth_replacement)




# Ask for user's input for 4 questions and save them into a list
# answers = []
# for question in parts_of_speech1:
# 	user_input= raw_input ("What's " + question + "? ")
# 	answers.append(user_input)
