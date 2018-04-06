"""
The Riddle:

The game Hip is played by two players using an N-by-N checkerboard.
Player 1 starts with N^2/2 white checkers and Player 2 with the
same number of black checkers. They take turns placing their checkers
on any of the board's empty squares. A player loses if any four of
his or her checkers form a square of any size, tilted to any angle.
(The game is purportedly named, of course, for hipsters' aversion
to squares.)

What is the largest board such that this game can end in a draw? What
does that draw look like?
"""

"""
My thought process:

To generate all possible boards of a given size:

Assume white goes first, so, if N is odd, white's number of checkers
is N^2/2, rounded up, and black's is rounded down.

So, make a linear list of length N^2 to represent the square board.
Then, think of the locations of the white checkers as a list of length
N^2/2, rounded up.  Then, we can make a list whose length is 1 longer
(call this the 'gap list'), it is the number of black checkers between
each adjacent pair of white checkers, plus an entry at the beginning for the
number of black checkers before the first white checker, and an entry at
the end for the number of black checkers after the last white checker.

In this gap list, each entry is greater than or equal to zero, and their
sum is exactly equal to the number of black checkers.  So, we will need to:
  1. Generate the list of all possible partitions of the number of black
    checkers.
  2. Pad this with zeroes so that the length of this is equal to the length
    of the gap list.
  3. Generate all possible permuations of this list.  In Python, the
    permutations function of the itertools is over-generous, it considers
    uniqueness of location not of value. (i.e. if we are generating
    permutations of (1,1,2), it considers the first 1 to be different from
    the second 1 because they are in different locations.)  So, we need
    to make a list of unique permutations by removing duplicates.

Then, we use this gap list to generate the board:
  1. Make a linear list of length N^2.
  2. For each entry of the gap list, put a number of black checkers (0's)
    into the board list (possibly none).
  3. Follow each entry of the gap list (except the last) with a white
    checker (a 1).
  4. Break up this list into N rows of length N, and this is your board.

To identify squares:
A square has four sides, opposite sides are parallel, adjacent are
  perpendicular.  All four sides have the same length.
If we compute [change in y, change in x] for a pair of points, and do *not*
  reduce the fraction, we get both slope and length at once.
So:
  1. For each player, make a list of the coordinates of each checker. 
  2. Generate a list of all pairs of points using itertools combinations.
    These are sorted lexicographically, with row having priority over column.
    (So, y then x, opposite of mathematical default.)
  3. For each pair, compute the pair [ch in y, ch in x].  Because of the sort,
    ch in y is always non-negative. 
  4. To get a square, need two pair of points that both have slope [ch in y,
    ch in x]. So, go through the list of slopes and find all the slopes that
    appear more than once.
  5. Find the two slopes that connect the first point of the first line to
    the two points of the second line.  Check if either of those slopes give
    both perpendicular direction and same length.
  6. If so, check the opposite pair.  If this pair also has perpendicular
    slope and same length, we've found a square!
"""

# We will need the permutations() and combinations() functions.
import itertools

# We will need the exit() function for debugging.
import sys

# This generates the partitions of n, grabbed from stackoverflow:
# http://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning
def partitions_dp(n):
    partitions_of = []
    partitions_of.append([()])
    partitions_of.append([(1,)])
    for num in range(2, n+1):
        ptitions = set()
        for i in range(num):
            for partition in partitions_of[i]:
                ptitions.add(tuple(sorted((num - i, ) + partition)))
        partitions_of.append(list(ptitions))
    return partitions_of[n]

# boardWidth is N in the original statement of the problem.
boardWidth = 5
boardSquares = boardWidth * boardWidth

boardCount = 0
noSquaresCount = 0

# If N is even, we need length N^2/2+1.  If N is odd, we need N^2/2+2,
#   because N^2/2 is rounded down by default.
if boardWidth % 2 == 0:
  gapListLength = boardSquares/2 + 1
else:
  gapListLength = boardSquares/2 + 2

# Generate the list of partitions
partitions = partitions_dp(boardSquares/2)

for partition in partitions:
  # First, pad with zeroes:
  baseGapList = []
  for entry in partition:
    baseGapList.append(entry)
  for i in range(gapListLength - len(partition)):
    baseGapList.append(0)
  # Update user.
  print "Working with partition:",
  print baseGapList
  # There may be a faster way to do the next two steps, but that's ok.
  # Now, generate all permutations.  There will be duplicates.
  gapListsDup = itertools.permutations(baseGapList)
  # Eliminate duplicates.
  gapLists = []
  for gapList in gapListsDup:
    if gapList not in gapLists:
      gapLists.append(gapList)
  # Update user.
  print "Generated", len(gapLists), "different gap lists."
  # Now, turn gap lists into boards, 0 = black, 1 = white
  # Each entry in the gap list = a number of black checkers
  for gapList in gapLists:
    # hasWhiteSquare and hasBlackSquare keep track of existence of squares
    hasWhiteSquare = False
    hasBlackSquare = False
    # First, generate the board as a 1-dimensional list
    boardList = []
    for entry in gapList:
      # Insert correct # of black checkers (possibly none)
      for i in range(entry):
        boardList.append(0)
      # Then a white checker
      boardList.append(1)
    # But last gap shouldn't end with a white checker, so remove the last one.
    boardList.pop()
    # Now, make it a 2-dimensional list
    board = [[boardList[boardWidth*j + i] for i in range(boardWidth)] for j in range(boardWidth)]
    # Check for squares.
    # Generate coordinate list for each player.
    # Notice that coords are given by (row, col), so (y,x)
    whiteCoords = []
    blackCoords = []
    for i in range(boardWidth):
      row = board[i]
      for j in range(boardWidth):
        if row[j] == 0:
          blackCoords.append((i,j))
        else:
          whiteCoords.append((i,j))
    # Each line segment is a pair of points
    whiteLinesComb = itertools.combinations(whiteCoords, 2)
    blackLinesComb = itertools.combinations(blackCoords, 2)
    # itertools objects don't support indexing, so convert to a list
    whiteLines = []
    blackLines = []
    for line in whiteLinesComb:
      whiteLines.append(line)
    for line in blackLinesComb:
      blackLines.append(line)
    # Each line segment has a slope & length given by (ch in y, ch in x)
    # Remember that y is first.
    whiteSlopes = []
    for line in whiteLines:
      point1 = line[0]
      point2 = line[1]
      slope = (point2[0] - point1[0], point2[1] - point1[1])
      whiteSlopes.append(slope)
    blackSlopes = []
    for line in blackLines:
      point1 = line[0]
      point2 = line[1]
      slope = (point2[0] - point1[0], point2[1] - point1[1])
      blackSlopes.append(slope)
    # Now look for a pair of line segments with the same slope & length.
    # This list has the index of each line in both the list of lines and
    #   in the list of slopes.
    whitePairs = []
    # For each line...
    for i in range(len(whiteSlopes)):
      # Go through the entries, see if it appears again later.  If so, append.
      for j in range(i+1, len(whiteSlopes)):
        if whiteSlopes[j] == whiteSlopes[i]:
            whitePairs.append((i, j))
    # Repeat for black
    blackPairs = []
    for i in range(len(blackSlopes)):
      for j in range(i+1, len(blackSlopes)):
        if blackSlopes[j] == blackSlopes[i]:
            blackPairs.append((i, j))
    # Now that we have the pairs, look for squares:
    for linePair in whitePairs:
      # First, find the four points in the pair of line segments:
      lineNum = linePair[0]
      line = whiteLines[lineNum]
      point0 = line[0]
      point1 = line[1]
      lineNum = linePair[1]
      line = whiteLines[lineNum]
      point2 = line[0]
      point3 = line[1]
      # Now, find the slope that we have stored,
      slope = whiteSlopes[lineNum]
      # and then compute the other two.
      slope1 = (point2[0] - point0[0], point2[1] - point0[1])
      slope2 = (point3[0] - point0[0], point3[1] - point0[1])
      # There are four ways that we could find a match:
      if (slope1[0] == -1*slope[1]) and (slope1[1] == slope[0]):
        slope3 = (point3[0] - point1[0], point3[1] - point1[1])
        if slope3 == slope1:
          hasWhiteSquare = True
      if (slope1[0] == slope[1]) and (slope1[1] == -1*slope[0]):
        slope3 = (point3[0] - point1[0], point3[1] - point1[1])
        if slope3 == slope1:
          hasWhiteSquare = True
      if (slope2[0] == -1*slope[1]) and (slope2[1] == slope[0]):
        slope4 = (point3[0] - point1[0], point3[1] - point1[1])
        if slope4 == slope2:
          hasWhiteSquare = True
      if (slope2[0] == slope[1]) and (slope2[1] == -1*slope[0]):
        slope4 = (point3[0] - point1[0], point3[1] - point1[1])
        if slope4 == slope2:
          hasWhiteSquare = True
    # Do it all again for black.
    for linePair in blackPairs:
      # First, find the four points in the pair of line segments:
      lineNum = linePair[0]
      line = blackLines[lineNum]
      point0 = line[0]
      point1 = line[1]
      lineNum = linePair[1]
      line = blackLines[lineNum]
      point2 = line[0]
      point3 = line[1]
      # Now, find the slope that we have stored,
      slope = blackSlopes[lineNum]
      # and then compute the other two.
      slope1 = (point2[0] - point0[0], point2[1] - point0[1])
      slope2 = (point3[0] - point0[0], point3[1] - point0[1])
      # There are four ways that we could find a match:
      if (slope1[0] == -1*slope[1]) and (slope1[1] == slope[0]):
        slope3 = (point3[0] - point1[0], point3[1] - point1[1])
        if slope3 == slope1:
          hasBlackSquare = True
      if (slope1[0] == slope[1]) and (slope1[1] == -1*slope[0]):
        slope3 = (point3[0] - point1[0], point3[1] - point1[1])
        if slope3 == slope1:
          hasBlackSquare = True
      if (slope2[0] == -1*slope[1]) and (slope2[1] == slope[0]):
        slope4 = (point3[0] - point1[0], point3[1] - point1[1])
        if slope4 == slope2:
          hasBlackSquare = True
      if (slope2[0] == slope[1]) and (slope2[1] == -1*slope[0]):
        slope4 = (point3[0] - point1[0], point3[1] - point1[1])
        if slope4 == slope2:
          hasBlackSquare = True
    boardCount += 1
    if not hasWhiteSquare and not hasBlackSquare:
      noSquaresCount += 1
  print "So far, found", noSquaresCount, "boards with no squares."
  print
##      print "No Squares in Board", boardCount, ":"
##      for row in board:
##        for entry in row:
##          print entry,
##        print
print "There were", noSquaresCount, "boards with no squares, out of", boardCount
