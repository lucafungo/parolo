import json
from random import randrange
import colorama
from colorama import Fore, Back


colorama.init(autoreset=True)
attempts = 0
attempted_letters = []

f = open('stored_words.json')
data = json.load(f)
word_of_the_day = data[randrange(1125)]

# Closing file
f.close()


def slicing(word):
    return [letter for letter in word]


f = open("intro.txt", "r")
print(f.read())




def check_attempt(word_of_the_day, word_by_user):
    global score
    score = 0
    count = 0
    yellow_letters = {}
    for user_letter in word_by_user:
        if user_letter == word_of_the_day[count]:
            print(Fore.BLACK+Back.GREEN + user_letter, end='')
            score = score + 1
            count = count + 1
        elif user_letter in word_of_the_day:
            if user_letter not in yellow_letters:
                print(Fore.BLACK+Back.YELLOW + user_letter, end='')
                yellow_letters[user_letter] = 1
            else:
                print(Fore.BLACK+Back.WHITE + user_letter, end='')
                attempted_letters.append(user_letter)
            count = count + 1
        else:
            print(Fore.BLACK+Back.WHITE + user_letter, end='')
            attempted_letters.append(user_letter)
            count = count + 1
    return score


slicing(word_of_the_day)

while attempts < 5:
    if attempts > 0:
        print(f"\n{attempted_letters}")
    word_by_user = input('\nType your guess: ')
    if len(word_by_user) == 5:
        if word_by_user not in data:
            print("Are you sure this word exist? Please type a new one.")
            continue
        slicing(word_by_user)
        check_attempt(word_of_the_day, word_by_user)
        attempts = attempts + 1
        if score == 5:
            print('\nYOU WON!\n')
            break
    elif len(word_by_user) == 1:
        if word_by_user.upper() == 'H':
            f = open("intro.txt", "r")
            print(f.read())
        elif word_by_user.upper() == 'R':
            break

    else:
        print('Please, type a five letters word.')

if attempts == 5 and score != 5:
    print(
        f'\n\nYOU LOSE! :( \n\nThe word to guess was {word_of_the_day.upper()}. Better luck next time!\n')
