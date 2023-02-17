import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


attempts = 0

word_of_the_day = 'abcde'


def slicing(word):
    return [letter for letter in word]


f = open("intro.txt", "r")
print(f.read())


def check_attempt(word_of_the_day, word_by_user):
    global score
    score = 0
    count = 0
    for user_letter in word_by_user:
        if user_letter == word_of_the_day[count]:
            print(Fore.BLACK+Back.GREEN + user_letter, end='')
            score = score + 1
            count = count + 1
        elif user_letter in word_of_the_day:
            print(Fore.BLACK+Back.YELLOW + user_letter, end='')
            count = count + 1
        else:
            print(Fore.BLACK+Back.WHITE + user_letter, end='')
            count = count + 1
    return score


slicing(word_of_the_day)

while attempts < 5:
    word_by_user = input('\nType your guess ')
    if len(word_by_user) == 5:
        slicing(word_by_user)
        check_attempt(word_of_the_day, word_by_user)
        attempts = attempts + 1
        if score == 5:
            print('\nYOU WON!\n')
            break
    else:
        print('Please, type a five letters word')

if attempts == 5 and score != 5:
    print('\n\nYOU LOSE!\n\nBetter luck next time!\n')
