import random

from words import Words
import string


def get_valid_word(Words):
    word = random.choice(Words)
    while '-' in word or '' in word:
        word = random.choice(Words)

    return word

def hangman():
    word = get_valid_word(Words)
    word_letters = set(word) # randomly chooses something from the list
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() # to keep track of what users have guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letter used
        #''.join(['a', 'b', 'c']) ---> 'a b c'
        print('You have ', lives,'You are used these letter', ''.join(used_letters))

        #what current word is (ie W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(word_list))
        user_letter = input('Guess a letter:  ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print('Letter not in the word;')

        elif user_letter in word_letters:
                print(f'You are have already used that character. Please try again')
        else:
            print('invalid character, Try again')  

    if lives == 0:
        print('You Died, Sorry')
    else:
        print('You Guessed the word', word, '!!')                
              
print(hangman)