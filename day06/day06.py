


def my_function(x):
    print('Hello')
    print('Bye')
    value = x
    print(value)
    
my_function(2)


my_function(400)



"""

#Hurdle 1 :

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move
    turn_right
    move()
    turn_right()
    move()
    turn_left()

for jumps in range(0,6):
    jump()

#--------------------------------

#Hurdle2 :
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move
    turn_right
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()
    


#-----------------------
#Hurdle3
def turn_right():
    turn_left()
    turn_left()
    turn_left()



def jump():
    turn_left()
    move()
    turn_right()
    move
    turn_right
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    if wall_in_front():
        jump()
    if front_is_clear():
        move()
    if at_goal():
        at_goal()

#-----------------------
#Hurdle4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    

while at_goal() != True:
    if wall_in_front():
        jump()
    if front_is_clear():
        move()
    if at_goal():
        at_goal()

"""





