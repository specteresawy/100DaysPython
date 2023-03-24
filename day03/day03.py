#Conditional Statements, Logical operators, CodeBlocks and scope
"""
if condition:
    do this
else:
    do this
"""

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#Nested If / else
"""
if condition:
    if another condition:
        do this:
    else :
        do this
else:
    do this
"""

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


bmi_value = weight / (height*height)
bmi_value = round(bmi_value)

if bmi_value < 18.5:
  health_condition = 'are underweight.'
elif bmi_value >= 18.5 and bmi_value <= 25:
  health_condition = 'have a normal weight.'
elif bmi_value > 25 and bmi_value < 30:
  health_condition = 'are slightly overweight.'
elif bmi_value > 30 and bmi_value < 35:
  health_condition = 'are obese.'
elif bmi_value > 35:
  health_condition = 'are clinically obese.'


print(f"Your BMI is {bmi_value}, you {health_condition}")

#Leapyear

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 != 0:
        print('Leap year.')
    elif year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else : 
            print('Not leap year.')      
else :
    print('Not leap year.')



#PizzaOrder

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S" or size == "s":
  bill = 15
elif size == "M" or size == "m":
  bill = 20
elif size == "L" or size == "l":
  bill = 25


if(add_pepperoni == "Y" and size == "S"):
  bill += 2
elif(add_pepperoni == "Y" and size == "M"):
  bill += 3
elif(add_pepperoni == "Y" and size == "L"):
  bill += 3
  
if extra_cheese == "Y":
  bill += 1


print(f"Your final bill is: ${bill}.")




#RollerCoaster

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


#Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
concName = name1+name2
concLowerName = concName.lower()

t = concLowerName.count("t")
r = concLowerName.count("r")
u = concLowerName.count("u")
e = concLowerName.count("e")
true = t + r + u + e
l = concLowerName.count("l")
o = concLowerName.count("o")
v = concLowerName.count("v")
e = concLowerName.count("e")

love = l + o + v + e

score = str(true) + str(love)

print(score)

score = int(score)



msg = ''
if score < 10 or score > 90:
  msg = 'you go together like coke and mentos.'
  print(f"Your score is {score}, {msg}")
elif score >= 40 and score <= 50:
  msg = 'you are alright together.'
  print(f"Your score is {score}, {msg}")
else:
  msg = score
  print(f"Your score is {score}.")


#Treasure Island

print(r"""
                       _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
                    
""")

print('Welcome to Treasure Island Your mission is to find the treasure')

user_choice = input("where do you want to go Left or Right")

if (user_choice == 'R') or (user_choice == 'Right') or (user_choice == 'r'):
    print('Game over')
if (user_choice == 'L') or (user_choice == 'Left') or (user_choice == 'l'):
    second_user_choice = input("Do you want to swim or wait")
    if ( second_user_choice == 'S') or (second_user_choice == 'swim'):
        print('Game over')
    else :
        third_user_choice = input("You came across three doors, Blue, Red and Yello ... Choose one B, R, Y")
        if (third_user_choice == 'B'):
            print('Game over')
        elif ( third_user_choice == 'Y'):
            print('You win')
        elif (third_user_choice == 'R'):
            print('Game over')
        else:
            print('wrong choice')


    


