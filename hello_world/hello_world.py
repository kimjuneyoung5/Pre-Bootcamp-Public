# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( "Hello, {{{name}}}" )	# with a comma
print( "Hello" + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( "Hello, {{{name}}}" )	# with a comma
print( "Hello" + "name" )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "My favorite food is {food}".format(food = fave_food1) ) # with .format()
print( F"{fave_food2} is my favorite food." ) # with an f string

