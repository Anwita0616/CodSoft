# TASK 4 ROCK-PAPER-SCISSORS GAME
import random
def playgame():
    print("Welcome to Rock-Paper-Scissors Game. You will be given 3 choices: Rock, Paper and Scissors.")
    print("Rock beats Scissors, Scissors beat Paper and Paper beats Rock. Type any choice you want. ")
    print("The game follows a best-of-three format and winner will be decided from that. Your opponent is the computer.")
    print("So, let's start the Game")
    score1 = 0
    score2 = 0
    for i in range(3):
        player1 = input("What do you choose: ").capitalize()
        array = ["Rock", "Paper", "Scissors"]
        player2 = random.choice(array)
        print("Player 1", player1)
        print("Player 2: ", player2)
        if player1 == player2:
            print("It's a tie")
        elif (player1 == "Rock" and player2 == "Scissors") or \
                (player1 == "Scissors" and player2 == "Paper") or \
                (player1 == "Paper" and player2 == "Rock"):
            print("You win !!")
            score1 += 1
        elif (player1 == "Scissors" and player2 == "Rock") or \
                (player1 == "Paper" and player2 == "Scissors") or \
                (player1 == "Rock" and player2 == "Paper"):
            print("Computer Wins !!")
            score2 += 1
        else:
            print("Invalid Choice !")
        print("Your Score: ", score1)
        print("Computer Score: ", score2)

    if score1 > score2:
        print("Congratulations !! You win the game !!")
    elif score2 > score1:
        print("Computer wins the game !!")
    else:
        print("It's a Tie !")
# prompt to play again
while True:
    playgame()
    p=input("Do you want to play again (Yes/No): ")
    if p == "no":
        print("Thank you for playing")
        break
    else:
        print("Let's play again")
