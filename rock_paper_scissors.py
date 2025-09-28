import random

#define score for user and computer
user_score = 0
computer_score = 0

#ask user guess until the user quit
options = ["rock", "paper", "scissors"]
while True:
    print("user score:",user_score)
    print("computer score:",computer_score)
    user_guess = input("Please type Scissor/Paper/Rock or q to quit the game: ").lower()
    if user_guess == "q":
        break    
    if user_guess not in options:
        print("please just Type Scissors/Paper/Rock")    
        continue
     #rock: 0, paper:1, scissors:2
    random_number = random.randint(0, 2)
    computer_guess = options[random_number]
    if user_guess == "rock" and computer_guess == "scissors":
        user_score += 1
    elif user_guess == "scissors" and computer_guess == "paper":
        user_score += 1
    elif user_guess == "paper" and computer_guess == "rock":
        user_score += 1    
    elif user_guess == computer_guess:
        print("u have a equal guess as computer, pick again")  
    else:
        computer_score += 1

if user_score > computer_score:
    print("congratulation! you won! and the scores are:" )
    print("user score:",user_score)
    print("computer score:",computer_score)
elif user_score == computer_score:
    print("It's a draw!" )
else:
    print("You lost!and i won!LOL")          

    
         