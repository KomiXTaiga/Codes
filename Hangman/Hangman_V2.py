import time
import random
from word_list import words

#make a word
def get_word():
    word = random.choice(words)
    return word
def playing(word):
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    tmp = input("Hey whats ur name! \n")
    print(f"Hey, {tmp} Lets play hangman!")
    print("Making word...")
    time.sleep(3)
    print(f"{word_complete} theres your letter of words!")
    while not guessed and tries>0:
        print(word_complete)
        print(f"You have {tries} left")
        guess = input("Please enter a letter!\n")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You alread guessed that letter, {guess}")
            elif guess not in word:
                print("Sorry this letter is not in your word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Godd Job you got 1 letter")
                guessed_letters.append(guess)
                word_as_list = list(word_complete)
                indicies = [i for i, letter in enumerate(word) if letter == guess]
                for i in indicies:
                    word_as_list[i] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha:
            if guess in guessed_words:
                print("You already guessed this word", guess)
            elif guess == word:
                print("Good job you won")
                guessed = True
            elif guess != word:
                print("Lmfao nah cuh that aint the word L 2 tries off for u being a straight dumbass")
                tries -= 2
                guessed_words.append(guess)
        else:
            print("Bruh that aint a letter")

    if guessed:
        print("You got it GG!")
    elif not guessed:
        print(f"LLLL YOU LOST SHIT AT THE GAME XD your word was {word}")
def main():
    word = get_word()
    playing(word)
    r = input("Play Again? (Y/N).")
    play_again = r.upper
    if play_again == 'Y':
        word = get_word()
        playing(word)
    else:
        pass
if __name__ == '__main__':
    main()


