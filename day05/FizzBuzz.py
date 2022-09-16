a = 1
b = 101

for numbers in range(a, b):
    if (numbers % 3 == 0 and numbers % 5 != 0):
        print('Fizz')
    elif(numbers % 3 != 0 and numbers % 5 == 0):
        print('Buzz')
    elif (numbers % 3 == 0 and numbers % 5 == 0):
        print('FizzBuzz')
    else:
        print(numbers)