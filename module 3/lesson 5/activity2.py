import random

while True:
    player =input("Enter a choic [Rock,Paper,Scissor]")
    position = ["Rock","Paper","Scissor"]
    computer = random.choice(position)
    print(f"\nYou choose {player} and Computer choose {computer}")

    if player == computer:
        print("\n Both player has been chosen same choice")

    elif player =="Rock":
        if computer =="Paper":
            print("Computer Wins .Try again!")
            print("Paper cover rock!")

        elif computer=="Scissor":
            print("You win")
            print("Rock destroy scissor")

    elif player =="Paper":
        if computer =="Scissor":
            print("Computer Wins .Try again!")
            print("Scissor cuts paper!")

        elif computer=="Rock":
            print("You win")
            print("Paper cover rock")

    elif player =="Scissor":
        if computer =="Rock":
            print("Computer Wins .Try again!")
            print("Rock destroys scissor!")

        elif computer=="Paper":
            print("You win")
            print("Scissor cuts paper")

    choice =input("Do you want to play again?(N/Y)>>")
    if choice =="N" or choice =="n":
        break