from random import choice

class Weapon(object):
  
  def __init__(self, name):
    self._losers = []
    self._winners = []
    self.name = name
    
  def __str__(self):
    return self.name
    
  def add_loser(self, other):
    if type(other) != type(self):
      raise TypeError('Can only add losers of type Weapon')
    elif other in self._winners:
      raise ValueError('Cannot add item to losers list because it is already in winners list.')
    
    else:      
      # Avoid infinite recursion
      if other not in self._losers:        
        self._losers.append(other)
        # Keep the symmetrical relationships in sync
        other.add_winner(self)
      
  def add_winner(self, other):
    if type(other) != type(self):
      raise TypeError('Can only add winners of type Weapon')
    elif other in self._losers:
      raise ValueError('Cannot add item to winners list because it is already in losers list.')
    
    else:
      # Keep the symmetrical relationships in sync
      other.add_loser(self)
      
      # Avoid infinite recursion
      if other not in self._winners:
        self._winners.append(other)  
        
  def get_loser(self):
    ''' Returns a randomly chosen loser from the _losers list. '''
    return choice(self._losers)
    
  def get_winner(self):
    ''' Returns a randomly chosen winner from the _winners list. ''' 
    return choice(self.winners) 
  
  def __gt__(self, other):
    """ Boolean method telling whether this weapon beats the other weapon.
    Overrides > operator """
    
    return other in self._losers
    
  def __lt__(self, other):
    """ Boolean method telling whether the other weapon beats this weapon.
    Overrides < operator """
    
    return other in self._winners
    
    
# Generate the standard rock, paper, and scissors weapons.
def get_standard_rps():
  rock = Weapon('Rock')
  paper = Weapon('Paper')
  scissors = Weapon('Scissors')
  
  rock.add_loser(scissors)
  paper.add_loser(rock)
  scissors.add_loser(paper)
  
  return rock, paper, scissors
  
  
# Generate the standard rock, paper, scissors, lizard, and spock weapons.
def get_standard_rpsls():
  pass
  #TODO
