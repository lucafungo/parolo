import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# print(Fore.BLACK+Back.GREEN + 'Hello word!')
# print(Fore.BLACK+Back.YELLOW + 'Hello word!')
# print(Fore.BLACK+Back.WHITE + 'Hello word!')

score = 0
attempts = 0

word_of_the_day = 'bipog'


def slicing(word):
    return [letter for letter in word]


def check_attempt(word_of_the_day, word_by_user):
    count = 0
    for user_letter in word_by_user:
        if user_letter == word_of_the_day[count]:
            print(Fore.BLACK+Back.GREEN + user_letter)
            count = count + 1
        elif user_letter in word_of_the_day:
            print(Fore.BLACK+Back.YELLOW + user_letter)
            count = count + 1
        else:
            print(Fore.BLACK+Back.WHITE + user_letter)
            count = count + 1


slicing(word_of_the_day)

while attempts < 5:
    word_by_user = input('Type your guess ')
    slicing(word_by_user)
    check_attempt(word_of_the_day, word_by_user)
    attempts = attempts + 1
    # print(slicing(word_by_user))
    # print(slicing(word_of_the_day))
    # print(attempts)
