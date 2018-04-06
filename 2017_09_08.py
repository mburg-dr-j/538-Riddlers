import random, time

def singlePlay (card1, card2):
  if numbers.index(card1[0]) > numbers.index(card2[0]):
    return 1
  elif numbers.index(card2[0]) > numbers.index(card1[0]):
    return 2
  else:
    return 0

def singleRound ():
  global hand1, hand2, stack
  result = singlePlay(stack[0], stack[1])
##  print(result)
  if result == 1:
    random.shuffle(stack)
    hand1 += stack
##    print (hand1)
  elif result == 2:
    random.shuffle(stack)
    hand2 += stack
##    print (hand2)
  else:
    runningOut = False
    if (len(hand1) == 0):
##      print('hand1 empty, so continue playing last card:', hand1)
##      print('stack:', stack)
      hand1.insert(0, stack.pop(1))
##      print('hand1 empty, so continue playing last card:', hand1)
##      print('stack:', stack)
      runningOut = True
    elif (len(hand2) == 0):
##      print('hand2 empty, so continue playing last card:', hand2)
##      print('stack:', stack)
      hand2.insert(0, stack.pop(0))
##      print('hand2 empty, so continue playing last card:', hand2)
##      print('stack:', stack)
      runningOut = True
    for i in range(3):
      if len(hand1) > 1:
        stack.insert(0, hand1.pop(0))
      else:
##        print ('hand1:', hand1)
##        print ('stack:', stack)
        runningOut = True
      if len(hand2) > 1:
        stack.insert(0, hand2.pop(0))
      else:
##        print ('hand2:', hand2)
##        print ('stack:', stack)
        runningOut = True
    stack.insert(0, hand1.pop(0))
    stack.insert(0, hand2.pop(0))
    if runningOut == True:
##      print('Final Stack:', stack)
      runningOut = False
      return
    singleRound()
  


suits = {'C':'Clubs', 'D':'Diamonds', 'H':'Hearts', 'S':'Spades'}
numbers = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'];


wins = [0, 0, 0]
startTime = round(time.time())
printed = False
##gameState = []
allRounds = 0
totalHands = 100000

while wins[0] + wins[1] < totalHands:
  hand1 = []
  hand2 = []
  rounds = 0
  for suit in suits.keys():
    for number in numbers:
      if number != 'A':
        hand2.append((number, suit))
      else:
        hand1.append((number, suit))
  random.shuffle(hand1)
  random.shuffle(hand2)
  while (len(hand1) > 0) and (len(hand2) > 0):
    rounds += 1
    stack = []
    stack.append(hand1.pop(0))
    stack.append(hand2.pop(0))
    singleRound()
##    if rounds > 10000:
##      print(hand1)
##      print(hand2)
##      print(rounds % 10000)
##      print()
##      if (hand1[0], hand2[0]) in gameState:
##        wins[2] += 1
##        break;
##      gameState.append((hand1[0], hand2[0]))                      
    if (round(time.time()) - startTime) % 60 == 0:
      if printed == False:      
        print (wins)
        printed = True
    if (round(time.time()) - startTime) % 60 == 1:
      printed = False
  if len(hand1) == 0:
    wins[1] += 1
##    if rounds > 2500:
##      print ('Long game, rounds = ', rounds, wins)
  elif len(hand2) == 0:
    wins[0] += 1
##    if rounds > 2500:
##      print ('Long game, rounds = ', rounds, wins)
  allRounds += rounds
print(wins, round(allRounds / totalHands))
