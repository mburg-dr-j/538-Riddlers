# Using Fraction and Decimal types to generate more exact comparisons
from fractions import Fraction
from decimal import *

# Using the product function from itertools to generate all the sequences
#   of digits that are possible for a given length.
from itertools import product

# Generate a list of all possible digits
digits = range(10)

# Check all sequences of digits of length ...
for prodLen in range(2,12):

  # Set the decimal precision to be equal to the number of digits we are at
  getcontext().prec = prodLen

  # Iterate through all possible sequences of the current length
  for dec in product(digits, repeat = prodLen):

    # Start running total for the fraction form
    a = Fraction(0, 1)

    # Iterate through the digits, add the appropriate fraction for the position
    for position in range(len(dec)):
      a += Fraction(dec[position], 10 ** position)

    # Form the decimal which is the average of the digits
    b = Decimal(sum(dec)) / Decimal(len(dec))

    # If the fraction and decimal are equal, send it to screen
    if a == b:
      if dec[-1] > 0:
        print(dec, a, b)

  # Update the user
  print ("Checked all sequences of length", prodLen)
