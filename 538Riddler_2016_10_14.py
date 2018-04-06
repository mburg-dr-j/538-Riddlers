rows = [[]]
probs = []
maxRows = 30
for row in range(6):
  rows[0].append(1)
for col in range(1,maxRows):
  rows.append([])
  for row in range(6*(col+1)):
    sum = 0
    column = rows[col-1]
    for prev in range(6):
      if row-prev-1 in range(len(column)):
        if row-prev-1 != 3 and row-prev-1 != 4:
          sum += column[row-prev-1]
    rows[col].append(sum)
##print rows
for row in range(maxRows):
  totalProb = 0
  for col in range(maxRows):
    if row < len(rows[col]):
      probTerm = rows[col][row] * 1.0
    else:
      probTerm = 0
    totalProb += probTerm / pow(6, col+1)
  probs.append(totalProb)
topThree = [0,0,0]
print topThree
for prob in probs:
  if prob > topThree[0]:
    topThree[0] = prob
    topThree.sort()
  print probs.index(prob) + 1, prob
probSurvival = 0
for prob in topThree:
  probSurvival += prob
print topThree, probSurvival
