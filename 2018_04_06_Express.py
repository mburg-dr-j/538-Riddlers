"""
I know this code is not good, it could be done better in a couple of ways:
   1. Use date objects instead of dealing with dates by hand.
   2. Just store a list of counts by year and then search the list
     instead of having to set up extra variables to track the figures
     we are looking for
   3. Definitely would've helped to set up a function or two.
     This is utterly linear.
"""

# I used 0 days in month 0 in order to simplify the indexing later
daysPerMo = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# This will keep track of attacks in one year, reset each year
yrCounts = []

# This will keep track of the number of days since the last attack
gap = 0

# This will keep track of the longest gap between attacks
maxGap = 0

# This will store the dates on either end of the longest gap
maxGapDate = []

# This will count the total number of attacks
totalCount = 0

# This keeps track of years with no attacks
emptyYears = []

# This keeps track of the date of the last attack so I can reference this
#   for the beginning of a gap
previousDate = [0, 0, 0]

# Loop through all years
for yr in range(100):

  # No attacks yet this year
  yrCount = 0

  # When outputting a single digit year, need to add a zero.
  if yr <= 9:
    yrStr = "0" + str(yr)
  else:
    yrStr = str(yr)
##  print ("Year: 20" + yrStr)

  # Loop through the 12 months.
  for mo in range(1, 13):

    # For non-leap years
    if yr % 4 != 0:

      # Loop through the days.
      for day in range(1, daysPerMo[mo] + 1):

        # Add 1 to the number of days since the last attack
        gap += 1

        # If an attack occurs
        if day * mo == yr:
##          print (str(mo) + "/" + str(day) + "/" + yrStr)

          # Add to the counts
          yrCount += 1
          totalCount += 1

          # If it is the longest so far, update
          if gap > maxGap:
            maxGap = gap
            maxGapDate = [mo, day, yr, previousDate]

          # I found out that the longest was 1096, wanted to see if there
          #  was more than one such gap.
          if gap == 1096:
            print ("Gap of length 1095; end date, start date:", maxGapDate)
            print()

          # Reset information about gaps because there was an attack
          gap = 0
          previousDate = [mo, day, yr]

    # Leap years
    else:

      # If it's not February
      if mo != 2:

        # Same as above
        for day in range(1, daysPerMo[mo] + 1):
          gap += 1
          if day * mo == yr:
##            print (str(mo) + "/" + str(day) + "/" + yrStr)
            yrCount += 1
            totalCount += 1
            if gap > maxGap:
              maxGap = gap
              maxGapDate = [mo, day, yr, previousDate]
            if gap == 1096:
              print ("Gap of length 1095; end date, start date:", maxGapDate)
              print()
            gap = 0
            previousDate = [mo, day, yr]

      # If it is February in a Leap Year
      else:

        # Same as above, but manually input 29 days.
        for day in range(1, 29):
          gap += 1
          if day * mo == yr:
##            print (str(mo) + "/" + str(day) + "/" + yrStr)
            yrCount += 1
            totalCount += 1
            previousDate = [mo, day, yr]
            if gap > maxGap:
              maxGap = gap
              maxGapDate = [mo, day, yr, previousDate]
            if gap == 1096:
              print ("Gap of length 1095; end date, start date:", maxGapDate)
              print ()
            gap = 0            
            previousDate = [mo, day, yr]
##  print ("Num of dates:", yrCount)

  # Now, done with the entire year, moving on to the next year.
  yrCounts.append(yrCount)
  if yrCount == 0:
    emptyYears.append(yr)

# Output results
myStr = ""

print ("Counts for each year:")
for i in range(100):

  # Put five years on each line
  myStr += str(i) + ", " + str(yrCounts[i]) + "   "
  if i % 5 == 4:
    print(myStr)
    myStr = ""

print()
print("Year with most attacks:", max(yrCounts))
print("Longest gap between attacks:", maxGap - 1)
print("End date, start date:", maxGapDate)
print("Total number of attacks:", totalCount)
print("Number of years with no attacks:", len(emptyYears))
print("List of these years:", emptyYears)
