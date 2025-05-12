choices = ["rock", "paper", "scissors"]
import random
computer_choice = random.choice(choices)

rock = "rock"
paper = "paper"
scissors = "scissors"
user_score = 0
computer_score = 0
while True:

    user_choice = input("Enter bewteen rock paper and sicossor: ")
    print("Computer chose:", computer_choice)
    if user_choice == rock and computer_choice == rock:
        print("You both choose rock so its a draw" ,'\n',"No points gained.")
        print ("User score: ",user_score)
        print("Computers score: ", computer_score)
        
    elif user_choice == rock and computer_choice == paper:
        print("Paper beats rock, paper wins!")
        computer_score +=1
        print("User score: ",user_score)
        print("Computers score: ",computer_score)
        
        
    elif user_choice == paper and computer_choice == rock:
        print("Paper beats rock, paper wins!")
        user_score +=1
        print("User score: ",user_score)
        print("Computers score: ",computer_score)
        
    elif user_choice == paper and computer_choice == paper:
        print("You both choose paper, so its a draw", '\n',"No points gained.")
        print("User score: ",user_score)
        print("Computers score: ",computer_score)
        
    elif user_choice == rock and computer_choice == scissors:
            print("Rock beats sicossor, So rock wins!")
            user_score +=1
            print("User score: ",user_score)
            print("Computers score: ",computer_score)
        
    elif user_choice == scissors and computer_choice == rock:
            print("Rock beats sicossor, So rock wins!")
            computer_score +=1
            print("User score: ",user_score)
            print("Computers score: ",computer_score)
        
    elif user_choice == scissors and computer_choice == scissors:
            print("You both choose sicossor, So its a draw", '\n',"No points gained")
            print("User score: ",user_score)
            print("Computers score: ",computer_score)
        
    elif user_choice == scissors and computer_choice == paper:
            print("Sicossor beats paper, sicossor wins.")
            user_score +=1
            print("User score: ",user_score)
            print("Computers score: ",computer_score)
        
    elif user_choice == paper and computer_choice == scissors:
            print("Sicossor beats paper, sicossor wins.")
            computer_score +=1
            print("User score: ",user_score)
            print("Computers score: ",computer_score)
            
    else:
        print("Please choose bewteen Rock, Paper and Scissors")
            
