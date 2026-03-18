import random 
print("Welcome to the game!!!")
print("x--------------x---------------x---------------x-------------x-----------x-------------x")

user_winns= 0 
computer_wins= 0
options =["rock","paper","scissors"]#options for the  game 


while True :
    user_input = input("enter one of these[{rock.paper,scissors} or Q to quit] : ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("please choose correct option")
        continue

    random_number = random.randint(0,2)
    #rock: 0,paper:1,scissors:2

    computer_pick = options[random_number]
    print("computer picked",computer_pick+".")
    #logic for game 
    if computer_pick == user_input:
        print("this is a tie!.. No one won")
    elif user_input == "rock" and computer_pick =="scissors":
        print("You Won!")
        user_winns += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_winns += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_winns += 1
    else:
        print("You  lose!")
        computer_wins += 1

print("x--------------x---------------x---------------x-------------x-----------x-------------x")
print("computer wins = ",computer_wins,"\n You won = ",user_winns)
print("x--------------x---------------x---------------x-------------x-----------x-------------x")


print("Goodbye!")
