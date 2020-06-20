# Stone Paper Scissor game

import random
print("Enter number of chanches:")
chance= int(input())
userscore=0
compscore=0

while(chance>0):
    print("Enter s-->Stone  p-->Paper   x-->Scissor")
    uinput=input()
    userinput=uinput[0].lower()
    if userinput=="s" or "p" or "x":
        cinp=random.randint(1,3)
        if cinp==1:
            compinp="s"
        elif cinp==2:
            compinp="p"
        elif cinp==3:
            compinp="x"

        if userinput==compinp:
            print("User entered-->", userinput)
            print("Computer entered-->",compinp)
            print("Your score is ", userscore)
            print("Computer score is ", compscore,"\n")
            chance=chance-1
        elif userinput=="s" and compinp=="p":
            print("User entered-->", userinput)
            print("Computer entered-->",compinp)
            compscore=compscore+1
            print("Your score is ", userscore)
            print("Computer score is ", compscore,"\n")
            chance=chance-1
        elif userinput=="s" and compinp=="x":
            print("User entered-->", userinput)
            print("Computer entered-->",compinp)
            userscore=userscore+1
            print("Your score is ", userscore)
            print("Computer score is ", compscore,"\n")
            chance=chance-1
        elif userinput=="p" and compinp=="s":
            print("User entered-->", userinput)
            print("Computer entered-->",compinp)
            userscore=userscore+1
            print("Your score is ", userscore)
            print("Computer score is ", compscore,"\n")
            chance=chance-1
        elif userinput=="p" and compinp=="x":
            print("User entered-->", userinput)
            print("Computer entered-->",compinp)
            compscore=compscore+1
            print("Your score is ", userscore)
            print("Computer score is ", compscore,"\n")
            chance=chance-1
        elif userinput=="x" and compinp=="s":
            print("User entered-->", userinput)
            print("Computer entered-->",compinp)
            userscore=userscore+1
            print("Your score is ", userscore)
            print("Computer score is ", compscore,"\n")
            chance=chance-1
        elif userinput=="x" and compinp=="p":
            print("User entered-->", userinput)
            print("Computer entered-->",compinp)
            userscore=userscore+1
            print("Your score is ", userscore)
            print("Computer score is ", compscore,"\n")
            chance=chance-1
        print("Chance left",chance)
    else:
        print("Enter valid input")

if userscore>compscore:
    print("You scored",userscore,". You win")
elif compscore>userscore:
    print("Computer wins", compscore,".")
else:
    print("Tie")
