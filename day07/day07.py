# Hangman Game 

import random
import requests

# the following variable holdes game image shape 



def get_list_of_words():
    response = requests.get(
        'https://www.mit.edu/~ecprice/wordlist.10000',
        timeout=10
    )

    string_of_words = response.content.decode('utf-8')

    list_of_words = string_of_words.splitlines()

    return list_of_words


words = get_list_of_words()

random_word = random.choice(words)

string = random_word
ph_word = []
ph_word[:] = string


game_img = (
""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     

"""
)
#HANGMANPICS array holds array of sequential images for the hangman
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



print(game_img)


# print(HANGMANPICS[0])
# print(HANGMANPICS[1])
# print(HANGMANPICS[2])
# print(HANGMANPICS[3])
# print(HANGMANPICS[4])
# print(HANGMANPICS[5])
# print(HANGMANPICS[6])

#print(f"random word is {random_word}")
# ph_word_len stores the word array length
ph_word_len = len(ph_word)
#creates a hidden array for the words with the same word length
hidden_array = ['-'] * ph_word_len 

#print(f"hidden array {hidden_array}")
#print(f"hidden array length :{len(hidden_array)}")
print(hidden_array)


#print(f" place holder word is : {ph_word}")
#print(f"place holder word length is {ph_word_len}")

trials = 0

def startgame(): 
  user_input = input('please enter a letter .. ')
  return user_input


usr_input = startgame()

print(f" user input {usr_input}")

trials = 0
max_trials = 7


def checkword(user_input, trials):
    
    if user_input in ph_word:
        for index, character in enumerate(ph_word):
            if character == user_input:
                hidden_array[index] = character
        print(hidden_array)
        if '-' not in hidden_array:
            print('You win')
        else:
          usr_input = startgame()
          checkword(usr_input,trials)
        
    else:
        if trials==max_trials:
            print(f'trials {trials}')
            print('Gameover')
        else:
          print(HANGMANPICS[trials])
          print(hidden_array)
          trials += 1
          usr_input = startgame()
          checkword(usr_input,trials)
        




checkword(usr_input,trials)

