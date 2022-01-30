from random import randint
import numpy as np
def main(int2):
    guess = False
    while guess == False:
        a = int(input("Please enter a number from 1,100 guess\n"))
        if a == int2:
            print("Good Job you guessed the number")
            guess = True
        elif a>int2:
            print("Nope lower")
        elif a<int2:
            print("Nope higher")
if __name__ == "__main__":
    int2 = randint(0,100)
    main(int2)
