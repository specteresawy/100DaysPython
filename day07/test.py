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
print(words)

random_word = random.choice(words)

random_word = random_word.split()

print(f"random word is {random_word}")

print(type(random_word))
