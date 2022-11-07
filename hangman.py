import random
from words import word_list
from art import stages
from art import opening


endGame = False
random_word = random.choice(word_list)
lives = 6

display = []
for c in range(len(random_word)):
    display+= "_"

print(opening)
while not endGame :
    guess = input("Guess a letter: ")

    if guess in display:
        print(f"You've already guessed {guess}")
    #will print the right guessed letter at their corresponding index
    for position in range(len(random_word)):
        letter = random_word[position]

        if letter == guess:
            display[position] = letter

    #Subtracts your lives whenever you enter a wrong letter
    if guess not in random_word:
        print(f"Letter '{guess}' is not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            endGame = True
            print("You lose.")
            print(f"The word is {random_word}")

    print(f"{' '.join(display)}")  #will turn the list into a string

    if "_" not in display:
        endGame = True
        print("You win.")

    print(stages[lives]) #Prints the ASCII art