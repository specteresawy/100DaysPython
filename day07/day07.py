# Hangman Game 



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


print(HANGMANPICS[0])
print(HANGMANPICS[1])
print(HANGMANPICS[2])
print(HANGMANPICS[3])
print(HANGMANPICS[4])
print(HANGMANPICS[5])
print(HANGMANPICS[6])


ph_word = ['c','a','s','t']

print(f" place holder world is : {ph_word}")

user_input = input('please enter a letter .. ')

if user_input in ph_word:
    print(f"letter {user_input} found in position {ph_word.index(user_input)}")
else:
    print('letter not found')
