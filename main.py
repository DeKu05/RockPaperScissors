import random  

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors):")
  options =["paper", "scissors", "rock"]
  computer_choice = random.choice(options)
  choices= {"player":player_choice,"computer":computer_choice}
  return choices

def check_win(player,computer):
  print(f"You chose {player}, Computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes Scissors! You Win!"
    else:
      return "Paper covers Rock! You loose."
  elif player == "paper":
    if computer == "scissors":
      return "Scissors Cuts Paper! You Loose."
    else:
      return "Paper covers Rock! You WIN!"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors Cuts Paper! You Win!."
    else:
      return "Rock smashes Scissors! You Loose."

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)  