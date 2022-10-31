import random

def get_choices():
    player_choice = input("Enter a choice (rocK, paper , scissor):")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player" :  player_choice , "computer" : computer_choice}
    return 
    print("rasheen")



def check_win(player, computer):
    print(f"You chose {player} , computer chose {playergi}")
    if player==computer:
        return "Its a tie"
    elif player=="rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win"
        else:
            return "Paper covers rock! You lose"
    elif player=="paper":
        if computer == "rock":
            return "Paper covers rock! You win"
        else:
            return "Scissors cuts paper! You lose"
    elif player=="scissor":
    
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print (result)