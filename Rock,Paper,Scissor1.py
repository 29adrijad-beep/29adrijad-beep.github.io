import random
import time
print("Welcome to Rock, Paper, Scissor")
plr=0
com=0

opt=["rock","paper","scissor"]
while True:
    input_player=input("Type\nRock\nPaper\nScissor\nQ to quit\n").lower()
    if input_player=="q":
        break
    elif input_player not in opt:
        break
    else:
        
       random_pick=random.randint(0,2)
       com_pick=opt[random_pick]
       print("The computer chooses....",com_pick,".")
       time.sleep(5)
       
    if input_player=="rock" and com_pick=="scissor":
         plr+=1
         print("Player wins ")
         time.sleep(5)
         
    elif input_player=="rock" and com_pick=="rock":
        print("Draw!")
        time.sleep(5)
    elif input_player=="scissor" and com_pick=="paper":
         plr+=1
         print("Player wins")
         time.sleep(5)
    elif input_player=="paper" and com_pick=="paper":
        print("Draw!!")
        time.sleep(5)
    elif input_player=="paper" and com_pick=="rock":
         plr+=1
         print("Player wins")
         time.sleep(5)
    elif input_player=="scissor" and com_pick=="scissor":
        print("Draw!!")
        time.sleep(5)
    else:
         print("Player wins\n Computer lost")
         com+=1
print("Player won",plr,"times")
print("Computer won",com,"time(s)")
time.sleep( 5)

print("Thank you for playing")
time.sleep( 5)

          

