#Write your code below this line 👇

def prime_checker(number):
    n = number
    y = n 
    num_lst = [] 
    while y >= 1:
        print(f"{n} % {y}  = {(n) % (y)}")
        res = n % y
        y -= 1
        num_lst.append(res)
    print(num_lst)
    indices = [i for i, x in enumerate(num_lst) if x == 0]
    if(len(indices)> 2):
        print("It's not a prime number.")
    else:
        print("It's a prime number.")  

        
          
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
