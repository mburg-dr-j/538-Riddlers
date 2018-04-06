import random

maxes = 0
samples = 100000
numTeams = 30
for i in range(samples):
  teamWins = []
  random.seed()
  for j in range(numTeams):
    teamWins.append(0)
  for j in range(numTeams):
    for k in range(162):
      if random.randrange(2) == 1:
        teamWins[j] += 1
##  print teamWins, max(teamWins)
  maxes += max(teamWins)
  if i % 1000 == 0:
    print '-',
    
print numTeams, " teams", samples, "samples", maxes*1.0/samples
  
