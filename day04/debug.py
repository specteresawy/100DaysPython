import random

#Rock Paper Scissors

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

computer_choice = random.randint(0,2)


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



print(f"user chose: {user_choice}")



print(f"computer chose :{computer_choice}")
