import random, heapq

workers = 5000

cups = []
mixedCups = []
totals = []

for i in range(workers):
  currCup = random.random()
  cups.append(currCup)
  mixedCups.append(currCup)
  totals.append(0)

for j in range(2000):
  random.shuffle(mixedCups)
##  print(cups)
##  print(mixedCups)

  remaining = 0
  for i in range(1 * workers):
    currCup = mixedCups[i % workers]
    cupIdx = cups.index(currCup)
    remaining += currCup
  ##  print (remaining)
    if remaining > 1:
      remaining = 0
##      print(cupIdx, currCup, remaining)
    else:
      totals[cupIdx] += currCup
##      print (cupIdx, currCup, remaining)

  print (j)
##  print (totals)
  topTotals = heapq.nlargest(10, totals)
  for i in range(10):
    print (topTotals[i], cups[totals.index(topTotals[i])])
