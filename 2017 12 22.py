# Left Right Center
# Game is:
# There are X players. Each starts with Y $1 bills.
# First Version: X = 6, Y = 3.
# Each player in turn rolls a die, 1,2 = Pass $1 to the player on your left
# 3,4 = Pass $1 to the player on your right. 5,6 = Put $1 in the middle.
# If only one player has any money left, game ends, that player gets all
# the money in the middle.
# The rules are vague, but I assume that a player is eliminated if they
# don't have a dollar to play with at the beginning of their turn.
# Conclusion 1: That player always gets all the money.

from random import randint

def gameOver(testDollars):
  # Test if game is over.
  # return True if only one player has any dollars left.
  # return False otherwise.
  numZeros = 0
  for entry in testDollars:
    if entry <= 0:
      numZeros += 1
  if numZeros == players - 1:
    return True
  else:
    return False

  # Initialize number of players and dollars per player
for players in range(2,21):
  startDollars = 3

  numGames = 1000000
  totalRounds = 0

  for i in range(numGames):
    
    # This list will contain the current state of the game --
    # dollars each player has on hand.
    dollars = []
    for player in range(players):
      dollars.append(startDollars)
    # middleDollars keeps track of how many dollars have been placed in the middle.
    middleDollars = 0

    # playerTurn keeps track of whose turn it is.
    playerTurn = 0

    # Each loop will be one player's turn.
    while not gameOver(dollars):

      # If the player is still in the game, pull out a dollar from their stash.
      if dollars[playerTurn % players] > -1:
        dollars[playerTurn % players] -= 1

      # Proceed only if they had a dollar to give.
      if dollars[playerTurn % players] > -1:

        # Roll the die.
        dieRoll = randint(0,6)

        # Left
        if dieRoll == 1 or dieRoll == 2:
          # Find the first player on the left who is still playing.
          destination = (playerTurn - 1) % players
          while dollars[destination] < 0:
            destination = (destination - 1) % players
          dollars[destination] += 1

        # Right
        elif dieRoll == 3 or dieRoll == 4:
          # Find the first player on the right who is still playing.
          destination = (playerTurn + 1) % players
          while dollars[destination] < 0:
            destination = (destination + 1) % players
          dollars[destination] += 1

        # Center
        else:
          middleDollars += 1

      playerTurn += 1
      # print (dollars, middleDollars)

    # print(playerTurn)
    totalRounds += playerTurn

  print(players, startDollars, totalRounds / numGames)
