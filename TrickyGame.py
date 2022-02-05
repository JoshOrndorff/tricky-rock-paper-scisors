from random import choice
from RPS import *
    
def get_user_move():
  move = None
  
  while move not in ['rock', 'paper', 'scisors', 'reset', 'exit']:
    cheating = False
    move = input("Choose 'rock', 'paper', 'scisors', 'reset', or 'exit': ")
    move = move.lower()
    if move[-1] == ' ':
      cheating = True
    move = move.strip()
    
  if move == 'rock':
    move = rock
  elif move == 'paper':
    move = paper
  elif move == 'scissors':
    move = scissors
  
  return move, cheating

# --------- Main Program -----------

rock, paper, scissors = get_standard_rps()

userMove = 'reset'

while userMove != 'exit':
  if userMove == 'reset':
    userScore = 0
    aiScore = 0
    print("Both scores have been reset.")
    
  else:
    
    # Figure out the AI's move
    if cheating:
      aiMove = userMove.get_loser()
    else:
      aiMove = choice([rock, paper, scissors])
      
    print("You chose {}, I chose {}.".format(userMove, aiMove))
    
    # Figure out who won
    if userMove > aiMove:
       print("You win!")
       userScore += 1       
       
    elif userMove < aiMove:
      print("I win!")
      aiScore += 1
  
  # Print the running scores  
  print("Human: {}\t\tAI: {}\n\n".format(userScore, aiScore))
     
  
  userMove, cheating = get_user_move()
  

