title = "Itsy-Bitsy Spider"
lyrics = "The itsy-bitsy spider climbed up the water spout. Down came the rain and washed the spider out. Out came the sun and dried up all the rain. And the itsy-bitsy spider climbed up the spout again"

quiz = "The itsy-bitsy _1____ climbed up the water _2___. Down came the _3__ and washed the spider out. Out came the _4__ and dried up all the rain. And the itsy-bitsy spider climbed up the spout again"

print quiz

first_replacement = "spider"
second_replacement = "spout"
third_replacement = "rain"
forth_replacement = "sun"

quiz = quiz.replace("_1____", first_replacement)
quiz = quiz.replace("_2___", second_replacement)
quiz = quiz.replace("_3__", third_replacement)
quiz = quiz.replace("_4__", forth_replacement)
print quiz