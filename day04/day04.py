# #Randomisation and Python lists
import random
import mymodule


random_integer = random.randint(0,10)
print(random_integer)

print(mymodule.pi)

print(random.random())


random_float = random.random()

random_float = random_float * 5

print(round(random_float))

random_side = random.randint(0,1)
if random_side == 1 :
    print('Heads')
else:
    print('Tails')

Lists

fruits = ['cherry', 'apple','bear']

print(fruits)
print(fruits[2])

fruits.append('kiwi')

fruits.extend(['orange','mango'])

print(fruits)



# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# """
# A random seed is used to ensure that results are reproducible.
# In other words, using this parameter makes sure that 
# anyone who re-runs your code will get the exact same outputs.
# Reproducibility is an extremely important concept in data science and other fields.
# https://www.geeksforgeeks.org/random-seed-in-python/
# """
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# choice = random.randint(0, len(names)-1)

# print(f"{names[choice]} is going to buy the Meal today.")


# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
print(f"first pos {position[0]}")
print(f"second pos {position[1]}")

colPos = position[0]
rowPos = position[1]

colPos = int(colPos)
rowPos = int(rowPos)

colPos = colPos-1
rowPos = rowPos-1

mark = 'x'

map[colPos][rowPos] = mark

print(f"{row1}\n{row2}\n{row3}")

#Rock Paper Scissors

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

computer_choice = random.randint(0,2)

computer_choice = str(computer_choice)

print(f"computer chose :{computer_choice}")

print(f"user chose: {user_choice}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


if user_choice == "0":
    user_choice = rock
elif user_choice == "1":
    user_choice = paper
elif user_choice == "2":
    user_choice = scissors


if computer_choice == "0":
    computer_choice = rock
elif computer_choice == "1":
    computer_choice = paper
elif computer_choice == "2":
    computer_choice = scissors



if computer_choice == rock:
    if user_choice == rock:
        print('Draw!')
    if user_choice == paper:
        print('User wins')
    if user_choice == scissors:
        print('Computer wins')
elif computer_choice == paper:
    if user_choice == paper:
        print('Draw!')
    if user_choice == scissors:
        print('User wins')
    if user_choice == rock:
        print('Computer wins')
elif computer_choice == scissors:
    if user_choice == scissors:
        print('Draw!')
    if user_choice == paper:
        print('Computer wins')
    if user_choice == rock:
        print('User wins')


print(f"user chose: {user_choice}")



print(f"computer chose :{computer_choice}")

