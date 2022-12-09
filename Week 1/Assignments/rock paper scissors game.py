#rock, paper, scissor game:
#1. Initialize the player's score and the number of times they have played.
#2. Then use while loop that continues until the player has played 5 times.
#3. Inside the loop, we ask the player to choose rock, paper, or scissors and generate the computer's move by randomly choosing one of the three options.
#4. We then use if-else statements to check for the different combinations of moves and determine a winner.
#5. If the player wins, their score is incremented by one. After the loop, we print the final score.

import random

# Initialize the player's score and number of times played
players_score = 0
computer_score = 0
times_played = 0

# Continue until the player has played 5 times
while times_played < 5:
#while times_played in range(5):
  # Asking the player for their actions
  player = input("Choose rock, paper, or scissors: ")

  # Generate the computer's move
  computer = random.choice(["rock", "paper", "scissors"])
  #print(f"\ncomputer choice is {computer},your choice is {player}\n")

  # Determine the winner
  if player == computer:
    print('*'*15)
    print("It's a tie!")
    print('*'*15)
  elif player == "rock" and computer == "scissors":
    print('*'*15)
    print("You win!")
    print('*'*15)
    players_score += 1
  elif player == "paper" and computer == "rock":
    print('*'*15)
    print("You win!")
    print('*'*15)
    players_score += 1
  elif player == "scissors" and computer == "paper":
    print('*'*15)
    print("You win!")
    print('*'*15)
    players_score += 1
  else:
    print('*'*15)
    print("You lose!")
    print('*'*15)
    computer_score += 1

  # Increment the number of times played
  times_played += 1

# Print the final score
print(f"Your final score is {players_score}.")
print(f"computer final score is {computer_score}.")