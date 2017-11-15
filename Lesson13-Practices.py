print "============== Practice3 List =============="
# Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5, 6]
list2.append([5, 6])

# to check, you can print them out using the print statements below.

print "showing list1 and list2:"
print list1
print list2


print "\n============== Practice 4 List =============="
# What is the difference between these two pieces of code?
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

def proc(mylist):
    mylist = mylist + [6, 7]

def proc2(mylist):
    mylist.append(6)
    mylist.append(7)

# Can you explain the results given by the print statements below?

print "demonstrating proc"
print list1
proc(list1)
print list1
print
print "demonstrating proc2"
print list2
proc2(list2)
print list2
print
# Python has a special assignment syntax: +=.  Here is an example:
	
list3 = [1,2,3,4,5]
# list3 += [6, 7]

# Does this behave like list1 = list1 + [6,7] or list2.append([6,7])? Write a
# procedure, proc3 similar to proc and proc2, but for +=. 
def proc3(mylist):
    mylist += [6,7]

print "demonstrating proc3"
print list3
proc3(list3)
print list3


print "\n============== Practice 5 While Loop =============="
# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data

# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.

# To create a random integer from 0 to 10, we first import the 
# "random" module

import random

# We then print a random integer using the random.randint(start, end) function
print "Random number generated: " + str(random.randint(0,10))

# Remember that if we want to concatenate a string and a number, we need to convert the 
# integer into a string using the str() function

# We now want to create a list filled with random numbers. The list should be 
# of length 20

random_list = []
list_length = 20

# Write code here and use a while loop to populate this list of random integers. A crucial
# function that will help you is to use the append() method to add elements to a list.
while len(random_list) < list_length:
   random_list.append(random.randint(0,10))

# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
print random_list


print "\n============== Practice 6 while Loop =============="
# Now, we want to ask ourselves the question: How many occurrences of 
# the number 9 appear in our randomly made list?
index = 0
count = 0
while index < len(random_list):
	if random_list[index] == 9:	
		count += 1
	index += 1

print "The occurrences of 9 is " + str(count)


print "\n============== Practice 7 while Loop =============="
# Great! We now want to create a new list that contains the counts
# of all occurrances of every number seen in the randomly generated 
# list. That means we want counts of all occurrences of all numbers
# from 0 through 10 in our randomly generated list.

# We can multiply a list construct to create a list with the same
# elements n number of times.
count_list = [0] * 11
# Check that we have a list of length 11 with all 0 elements
print count_list

index = 0
# Write code here to loop through every number in random_list and
# update count_list appropriately
while index < len(random_list):
	value = random_list[index]
	count_list[value] += 1
	index += 1

# Check the list we created
print count_list
# If we coded everything correctly, the sum of all of the numbers 
# in count_list should be 20
print sum(count_list)



print "\n============== Practice 7 while Loop =============="
# We now would like to summarize this data and make it more visually appealing
# We want to go through count_list and print a table that shows the number and its 
# corresponding count.

# The output should look like this neatly formatted table:
"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""


index = 0
number_spaces = 0
number_len = len("number")

print "number | occurrence"

while index < len(count_list):
	count = count_list[index]
	number_spaces = number_len - len(str(index))
	print number_spaces * " " + str(index) + " | " + str(count) 
	index = index + 1

print "\nReplace the count with a string of asterisks"

index = 0
while index < len(count_list):
    count = count_list[index]
    number_spaces = number_len - len(str(index))
    print number_spaces * " " + str(index) + " | " + "*" * count
    index = index + 1


print "\n============== Practice 9 Product_list =============="
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

# def product_list(list_of_numbers):
#     index = 0
#     result = 1
#     while index < len(list_of_numbers):
#         result *= list_of_numbers[index]
#         index += 1
#     return result

def product_list(list_of_numbers):
    result = 1
    for i in list_of_numbers:
        result *= i
    return result

print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1


print "\n============== Practice 11 Split =============="
# Let's play around with one more string method: string.split(), which
# splits a string into a list of substrings, and returns it as a new list. 
# Assign list_of_words1 to the split string1 and list_of_words2 to the split string2.

string1 = "Yesterday, PERSON and I went to the PLACE. On our way, we saw a ADJECTIVE NOUN on a bike."
string2 = "PLACE is located on the ADVERB side of Dublin, near the mainly ADJECTIVE areas of PLACE."
list_of_words1 = string1.split()
list_of_words2 = string2.split()
print list_of_words1
print list_of_words2

print "\n============== Practice 12 Join =============="
print "-".join(list_of_words1)
print "*".join(list_of_words2)


print "\n============== Practice 13 Word Position =============="
# Here's another chance to practice your for loop skills. Write code for the 
# function word_in_pos (meaning word in parts_of_speech), which takes in a string 
# word and a list parts_of_speech as inputs. If there is a word in parts_of_speech
# that is a substring of the variable word, then return that word in parts_of_speech, 
# else return None.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None


test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]

print word_in_pos(test_cases[0], parts_of_speech)
print word_in_pos(test_cases[1], parts_of_speech)
print word_in_pos(test_cases[2], parts_of_speech)
print word_in_pos(test_cases[3], parts_of_speech)


print "\n============== Practice 14 Word Position =============="
# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            word = word.replace(replacement, "Corgi")
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_game(test_string, parts_of_speech)  


print "\n============== Practice 15 Raw input =============="
# A list of replacement words to be passed in to the play game function. 
parts_of_speech1  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN", "NAME", "VERB", "OCCUPATION", "ADJECTIVE"]

# The following are some test strings to pass in to the play_game function.
test_string1 = "Hi, my name is NAME and I really like to VERB PLURALNOUN. I'm also a OCCUPATION at PLACE."
test_string2 = """PERSON! What is PERSON going to do with all these ADJECTIVE PLURALNOUN? Only a registered 
OCCUPATION could VERB them."""
test_string3 = "What a ADJECTIVE day! I can VERB the day off from being a OCCUPATION and go VERB at PLACE."

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
# Plays a full game of mad_libs. A player is prompted to replace words in ml_string, 
# which appear in parts_of_speech with their own words.  
def play_game(ml_string, parts_of_speech):    
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("Type in a: " + replacement + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced
    
print play_game(test_string1, parts_of_speech1)         

