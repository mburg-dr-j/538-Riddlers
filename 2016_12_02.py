import random, itertools

numTeams = 30
numYears = 10000000
winners = [random.randrange(0,numTeams) for i in range(numYears)]
losingStreaks = [0] * numTeams

brokenStreaks = []

years108 = 0

for winner in winners:
##  print winner,
  longestStreak = max(losingStreaks)
  for team in range(numTeams):
    if team == winner:
      losingStreaks[team] = 0
    else:
      losingStreaks[team] += 1
  if max(losingStreaks) < longestStreak:
##    print "Streak Broken!",
    brokenStreaks.append(longestStreak)
  if max(losingStreaks) > 107:
    years108 += 1
##  print losingStreaks

##print brokenStreaks
print float(sum(brokenStreaks))/float(len(brokenStreaks))
print min(brokenStreaks), max(brokenStreaks)
print float(years108)/float(numYears)
