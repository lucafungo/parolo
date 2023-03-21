import json
from random import randrange
import colorama
from colorama import Fore, Back

# Initialize colorama to enable colored text in the terminal
colorama.init(autoreset=True)

# Set the number of attempts to 0 and create an empty list to store attempted letters
attempts = 0
attempted_letters = []

# Open the file containing the words to guess and select a random word
f = open('stored_words.json')
data = json.load(f)
word_of_the_day = data[randrange(1125)]

# Close the file
f.close()

# Define a function to convert a word into a list of letters
def slicing(word):
    return [letter for letter in word]

# Open and print the contents of the intro file
f = open("intro.txt", "r")
print(f.read())

# Define a function to check the user's attempt against the word of the day
def check_attempt(word_of_the_day, word_by_user):
    global score
    score = 0
    count = 0
    yellow_letters = {}
    for user_letter in word_by_user:
        if user_letter == word_of_the_day[count]:
            # Print the correctly guessed letter in green
            print(Fore.BLACK+Back.GREEN + user_letter, end='')
            score = score + 1
            count = count + 1
        elif user_letter in word_of_the_day:
            if user_letter not in yellow_letters:
                # Print the incorrectly guessed letter in yellow
                print(Fore.BLACK+Back.YELLOW + user_letter, end='')
                yellow_letters[user_letter] = 1
            else:
                # Print the letter that has already been attempted in white
                print(Fore.BLACK+Back.WHITE + user_letter, end='')
                attempted_letters.append(user_letter)
            count = count + 1
        else:
            # Print the incorrectly guessed letter in white
            print(Fore.BLACK+Back.WHITE + user_letter, end='')
            attempted_letters.append(user_letter)
            count = count + 1
    return score

# Convert the word of the day into a list of letters
slicing(word_of_the_day)

# Allow the user to attempt to guess the word of the day 6 times
while attempts < 6:
    if attempts > 0:
        # Print any attempted letters that were not in the word of the day
        print(f"\n{attempted_letters}")
    word_by_user = input('\nType your guess: ')
    if len(word_by_user) == 5:
        if word_by_user not in data:
            # If the user's attempt is not a valid word, prompt them to try again
            print("Are you sure this word exist? Please type a new one.")
            continue
        # Convert the user's attempt into a list of letters and check it against the word of the day
        slicing(word_by_user)
        check_attempt(word_of_the_day, word_by_user)
        attempts = attempts + 1
        if score == 5:
            # If the user correctly guesses all letters, print a victory message and end the game
            print('\nYOU WON!\n')
            break
    elif len(word_by_user) == 1:
        if word_by_user.upper() == 'H':
            # If the user enters 'H', reprint the intro text
            f = open("intro.txt", "r")
            print(f.read())
        elif word_by_user.upper() == 'R':
            break

    else:
        # If the user atttempt is a word of more or less letters then five, print this an error
        print('Please, type a five letters word.')
# If the user reach five attempts correctly guess the 'word_of_the_day', end the game and print this 
if attempts == 6 and score != 5:
    print(
        f'\n\nYOU LOSE! :( \n\nThe word to guess was {word_of_the_day.upper()}. Better luck next time!\n')

