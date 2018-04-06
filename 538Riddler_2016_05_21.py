import random

reps = 1000000
totalCommon = [0,0,0]
countSteps = [0,0,0]

for i in range(reps):
  poss = []
  done = False
  while not done:
    j = random.randrange(6)
    if j in [0,1,2]:
      gem = 0
    elif j in [3,4]:
      gem = 1
    else:
      gem = 2
    poss.append(gem)
    if (0 in poss) and (1 in poss) and (2 in poss): 
      done = True
##  print poss, poss.count(0)
  while len(totalCommon) < len(poss)+1:
    totalCommon.append(0)
    countSteps.append(0)
  totalCommon[len(poss)] += poss.count(0)
  countSteps[len(poss)] += 1
print totalCommon
print countSteps
print len(countSteps)
print sum(totalCommon)
