# #DataTypes

# #String
# #Subscripting:
# print('Hello'[0])
# print('Hello'[2])
# print('Hello'[4])
# print('Hello'[1])
# #concatenation:
# print('Hello' + ' World!')
# print('123'+'556')
# # Integer
# #Large Integers
# print(123_456_789)
# #Float
# 3.14159

# #Boolean
# True
# False


# #Type checking:
# type(num_char)
# type(str(num_char))


# #Type conversion, type casting


# num_char = len(input("what is your name? "))
# new_num_char = str(num_char)
# print("your name has " + new_num_char + " chars")

# #Conversion can be for other datatypes not just str and int

# float(124)



# #----------
# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇

# first_digit = two_digit_number[0]

# first_digit = int(first_digit)

# second_digit = two_digit_number[1]

# second_digit = int(second_digit)

# result = first_digit + second_digit 

# print(result)


# #Mathematical operations in Python
# #---------------------------------
# #addition 
# print(4+5)
# #subtraction
# print(7-2)
# #multiplication
# print(2*2)
# #division, result in float
# print(6/3)
# #exponent, 2**3 = 2*2*2
# 2**3
# #order of operations PEMDAS
# #PEMDAS : Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right).

# #Excersise 2

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# height = float(height)
# height_squared = height * height

# bmi =  float(weight) / height_squared 

# print(int(bmi))



# #Rounding numbers
# result = 8/3
# print(result)

# result = round(result,2) #2 decimal places

# print(result)

# #Floor Division
# print(8 // 3) #floor division results in int datatype


# #shorthand for addition, sub..., mul..., div...
# score = 2
# score += 2
# score -= 2 
# score *= 2
# score /= 2

# #Fstrings

# score = 0
# height = 1.8
# isWinning = True
# print(f"Your score is {score} and your height is {height} and you are winning condition is {isWinning}")


# #life in weeks

# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# age = int(age)
# age_in_days = age * 365
# age_in_weeks = age * 52
# age_in_months = age * 12
# #1 year = 365 days, 1 year = 52 weeks, 1 year = 12 months
# max_age_in_days = 90 * 365
# max_age_in_weeks = 90 * 52
# max_age_in_months= 90 * 12

# left_age_in_days = max_age_in_days - age_in_days 
# left_age_in_weeks = max_age_in_weeks - age_in_weeks
# left_age_in_months = max_age_in_months - age_in_months
# # you have x days, y weeks and z months left 

# print(f"You have {left_age_in_days} days, {left_age_in_weeks} weeks, and {left_age_in_months} months left")


#Tip calculator
print('Welcome to the Tip calculator')

totalBill = input('What was the total bill?')
totalBill = float(totalBill)
print(f"total bill {totalBill}")

tipPercentage = input('What % tip would you like to give? 10, 12 or 15?')
tipPercentage = float(tipPercentage)
tipPercentage /= 100
tipAmount = totalBill * tipPercentage

print(f"tipAmount {tipAmount}")
totalBill += tipAmount

numOfPeople = input('How many people to split the bill?')
numOfPeople = int(numOfPeople)
print(f"num of people {numOfPeople}")

result = totalBill / numOfPeople
result = round(result,2)
print(f"Each Person should pay{result}")



