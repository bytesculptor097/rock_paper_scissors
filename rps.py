# Importing the random generator library 
import random as r
# Importing the the time library for delaying for 1.5
import time
# The 3 hands
hands = ('rock ✊', 'paper 🖐️', 'scissors ✌️')
random_hand = r.choice(hands)

# Game definition
def play_rps():
    global random_hand, hands
    print("\t\t------Welcome to Rock, Paper, Scissors!------")
    user_hand = str(input("Enter rock, paper, or scissors: "))
    if user_hand == 'rock':
        user_hand = hands[0]
    elif user_hand == 'paper':
        user_hand = hands[1]
    elif user_hand == 'scissors':
        user_hand = hands[2]   
    else:
        print("Invalid input. Please try again.")
        return play_rps()
    
    print("\nYou chose:", user_hand)
    print("\nComputer chose:", random_hand)
    time.sleep(1.5)
    if user_hand == "rock ✊" and random_hand == "scissors ✌️":
        print("\nYou win! Rock beats scissors.")
    elif user_hand == "rock ✊" and random_hand == "paper 🖐️":
        print("\nYou lose! Paper beats rock.")
    elif user_hand == "paper 🖐️" and random_hand == "rock ✊":
        print("\nYou win! Paper beats rock.")
    elif user_hand == "paper 🖐️" and random_hand == "scissors ✌️":
        print("\nYou lose! Scissors beats paper.")
    elif user_hand == "scissors ✌️" and random_hand == "paper":
        print("\nYou win! Scissors beats paper.")
    elif user_hand == "scissors ✌️" and random_hand == "rock ✊":
        print("\nYou lose! Rock beats scissors.")
    else:
        print("\nIt's a tie! You both chose", user_hand)
# Clling the play_rps definition
play_rps()
    


