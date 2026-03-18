import turtle # turtel module is built -in module python 
import time # time module 
import random # random module 



WIDTH , HEIGHT = 700, 600 # this is the size of the panel we are using for the game 

COLORS= ['red','yellow','cyan','orange','black','blue','pink','green','purple','brown'] # this is the options for the colours we are using till now for different racers in the race of turtles

print("Welcome to this amazing game !!")
def get_number_of_racers():# it is a function for the number of racers we want to use 
    racers = 0
    while True:
        racers = input("Enter the number of racer do you want to race [2-10] :  ")
        if racers.isdigit():# function will put this in the str so we are writing a code so it can be int so if it is not program will crash out

            racers = int(racers)
        else:
            print('Input is not the numeric... Please try again ')
            continue

        if 2<= racers <=10:
           return racers
        
        else:
            print("Number is invalid range should be in range 2-10")


def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randint(1,20)
            
            racer.forward(distance)


            x, y = racer.pos()
            if y  >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]



def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i , color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i +1)*spacingx, -HEIGHT//2 + 20 )        
        racer.pendown()
        turtles.append(racer)
    return turtles




def init_turtle():# this is the function writed for the turtle game screen or  you can say graphics
    screen  = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing game 🐢🐢')
     
racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]#: = this sign means no of racers we are getting
winner=race(colors)
print(f"the winner of the turtle race is  color :{winner}")
time.sleep(5)








