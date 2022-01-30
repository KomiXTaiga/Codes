from random import randint
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#making a new word + making that word into a list
r = randint(0,2)
new_word = word_list[r]
x = True
lst = list(new_word)
a = 0

z = 0
while(x == True):
    z += 1
    if z == 6:
        x = False
    tmp = input("\nPlease guess a letter\n")
    guess = tmp.lower()
    print(" ")
    for i in range(len(lst)):
        if lst[i] == guess:
            print(lst[i])
        else:
            print("wrong")

