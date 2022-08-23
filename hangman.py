import random

from words import Words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(Words):
    word = random.choice(Words)
    while '-' in word or '' in word:
        word = random.choice(Words)

    return word.upper()

def hangman():
    word = get_valid_word(Words)
    word_letters = set(word) # randomly chooses something from the list
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() # to keep track of what users have guessed

    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letter used
        #''.join(['a', 'b', 'c']) ---> 'a b c'
        print('You have ', lives,'You are used these letter', ''.join(used_letters))

        #what current word is (ie W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ''.join(word_list))
        user_letter = input('Guess a letter:  ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives -1
                print('\nLetter', user_letter, 'is not in the word')

        elif user_letter in word_letters:
                print(f'You are have already used that character. Please try again')
        else:
            print('\ninvalid character, Try again')  

    if lives == 0:
        print(lives_visual_dict[lives])
        print('You Died, Sorry')
    else:
        print('You Guessed the word', word, '!!')                
              
if __name__ == '__main__':
    hangman()