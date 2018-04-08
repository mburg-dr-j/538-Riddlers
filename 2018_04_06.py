"""
From Matt Gold, a chance, perhaps, to redeem your busted bracket:

On Monday, Villanova won the NCAA men’s basketball national title. But
I recently overheard some boisterous Butler fans calling themselves the
"transitive national champions," because Butler beat Villanova earlier
in the season. Of course, other teams also beat Butler during the season
and their fans could therefore make exactly the same claim.

How many transitive national champions were there this season? Or, maybe
more descriptively, how many teams weren’t transitive national champions?

(All of this season’s college basketball results are here. To get you
started, Villanova lost to Butler, St. John’s, Providence and Creighton
this season, all of whom can claim a transitive title. But remember, teams
beat those teams, too.)
"""

# Gonna need Regular Expressions to parse that input file
import re

def findTransChamps(teamIndex):
  """
  We'll do this recursively
  """
  # Need the global transChamps list, we'll be adding to it
  global transChamps, searched
  for game in games:
    if game[1] == teamIndex:
#      print (teams[game[0]], "def", teams[game[1]])
      if game[0] not in transChamps:
        transChamps.append(game[0])
      if game[0] not in searched:
        searched.append(game[0])
        findTransChamps(game[0])


# input file
dataFile = "./2018_04_06_data.txt"
data = open(dataFile, 'r')

# Set up ordered list of teams and games
teams = []
games = []

# Each team may have letters, spaces, @, ', & or . in it.
# It might also have - in it, which is a problem because the date also does.
# So we require one or more of the other characters first, then
#   possibly a - character.  This avoids matching the dates.
teamRegExp = re.compile("[@.'&A-Za-z\s]{1,}[@.'&\-A-Za-z\s]+")

# Each score is just digits
scoreRegExp = re.compile('[0-9]+')

# Reading through the lines of the file
for line in data:

  # Find the first team, convert to a string
  team1Raw = teamRegExp.search(line)
  team1 = team1Raw.group(0).strip()

  # Find the first score, convert to an integer
  score1Match = scoreRegExp.search(line, team1Raw.end())
  score1 = int(score1Match.group(0))

  # Find the second team, convert to a string
  team2Raw = teamRegExp.search(line, score1Match.end())
  team2 = team2Raw.group(0).strip()

  #Find the second team, convert to a string
  score2Match = scoreRegExp.search(line, team2Raw.end())
  score2 = int(score2Match.group(0))

  # The try...except was helpful in debugging, probably unnecessary now
  # Strip out the @ symbol if present so that we have just the team name
  # This is important to make sure that teams match
  try:
    if team1[0] == "@":
      team1 = team1[1:]
  except:
    print(i, "  ", line)
  try:
    if team2[0] == "@":
      team2 = team2[1:]
  except:
    print(i, "  ", line)

  # Check if we've seen these teams before, add them to the list if not
  if team1 not in teams:
    teams.append(team1)
  if team2 not in teams:
    teams.append(team2)

  # Find out where they are in the list
  team1Index = teams.index(team1)
  team2Index = teams.index(team2)

  # I don't think ties are possible, but we'd better be safe
  if score1 == score2:
    print('We have a tie.')
    break

  # It looks like the winner is first on all of these, but just to be safe
  if score1 > score2:
    game = [team1Index, team2Index]
  else:
    game = [team2Index, team1Index]
  games.append(game)

# Just checking   
print (len(teams))
print (len(games))

###############
# Now we've read in all the data
###############

# Start to track down transitive champions
transChamps = []

# Need to keep track of who we've searched, only check each team once
# This avoids circular searches in the recursion
searched = []

# Gget the ball rolling
nova = teams.index('Villanova')
findTransChamps(nova)

print ("There are", len(transChamps), "transitive champions.")

# Make list of teams that are not transitive champions
notTransChamps = [team for team in teams if teams.index(team) not in transChamps]

print ("There are ", len(notTransChamps), "teams that are not transitive champions.")

print(*notTransChamps, sep=", ")
