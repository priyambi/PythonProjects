import random
actions=["Rock","Scissor","Paper"]
print("ROCK-PAPER-SCISSOR GAME")
print("Let's Begin")
while True:
    player=input("What is your move: Rock, Scissor or Paper? ")
    computer=random.choice(actions)
    if(player==computer):
        print("Try again")
    elif(player=="Rock" and computer=="Paper"):
        print("Computer chose ",computer," and Computer Wins")
        break
    elif(player=="Rock" and computer=="Scissor"):
        print("Computer chose ",computer," and Player Wins")
        break
    elif(player=="Scissor" and computer=="Paper"):
        print("Computer chose ",computer," and Player Wins")
        break
    elif(player=="Scissor" and computer=="Rock"):
        print("Computer chose ",computer," and Computer Wins")
        break
    elif(player=="Paper" and computer=="Rock"):
        print("Computer chose ",computer," and Player Wins")
        break
    elif(player=="Paper" and computer=="Scissor"):
        print("Computer chose ",computer," and Computer Wins")
        break
print("Game Over")
    



