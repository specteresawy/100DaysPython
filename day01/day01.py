"""
String Manipulation, 
"""
#print function print()
#----------------------
#New line
print('Hello world! \nHello world!')
#Concatenate
print('Hello'+' '+'Angela')
#tab
print('Hello\tworld')
print('Hello   world')

#input function ()
#----------------
input('What is your name?')

#nested input fn inside print fn
print("Hello " + input("what is your name ? "))


#Exercise#1
#Write your code below this line 👇
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")




#len function()
#---------------
print(len("sam"))
print(len(input('what is your name ?')))

#variables
#----------
name = input('What is your name ?')
print(len(name))

#Excercise-4 variables:
#-----------------------


# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


#Day1, Project: BandName Generator

#1. Create a greeting for your program.

userName = input('Please Enter your name: ....')
print('Hello ' + userName + ' and Welcome to the BandName Generator')


#2. Ask the user for the city that they grew up in.
userCityName = input("Please Enter the City's name you grew up in ")

#3. Ask the user for the name of a pet.

userPetName = input("Please Enter your pet's name ")
#4. Combine the name of their city and pet and show them their band name.
bandName = userCityName+userPetName
#5. Make sure the input cursor shows on a new line:
print("\n your Band's Name is : "+ bandName)
