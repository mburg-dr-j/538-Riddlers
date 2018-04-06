import random

PATH = '/Users/ma/Documents/Python/538 Riddlers/'
fin = open(PATH + 'enable1.txt')
word_index = []
word_list = []
totalFreqs = []

def buildWordIndex():
"""
Builds a word list and an index of all the letters and their positions.
word_list = just a list of every word.
word_index = contains 26 lists, one for each letter.  Each letter has a
  list, first entry is a list of all words (by index in word list) that
  have this letter as first letter, then second entry is a list of all
  words that have this letter as econd letter, etc.
"""
  for index in range(26):
    word_index.append([])
  maxWords = 10
  words = 0
  for word in fin:
    word = word[:-2]
    word_list.append(word)
    for index in range(len(word)):
      if (ord(word[index]) > 96) and (ord(word[index]) < 123):
        charNum = ord(word[index]) - 97
        while len(word_index[charNum]) <= index:
          word_index[charNum].append([])
        word_index[charNum][index].append(words)
    words += 1

def countFreqs():
"""
Counts total appearances of each letter.
Includes multiplicity (so multiple occurances of a letter in a single word
  count multiplt times.)
"""
  letter = 97
  loc = 0
  for letterList in word_index:
    totalFreq = 0
    for letterLoc in letterList:
  ##    print chr(letter), loc, len(letterLoc)
      totalFreq += len(letterLoc)
      loc += 1
    totalFreqs.append(totalFreq)
    letter += 1
    loc = 0

def generateProbs():
"""
Goes through the frequencies, sorts most frequent -> least (mostly out
  of curiosity), and then converts frequency to proportion out of 10k.
"""
  total = 0
  freqsInOrder = []
  for i in range(26):
    maxFreq = 0
    for j in range(26):
      if totalFreqs[j] > maxFreq:
        maxFreq = totalFreqs[j]
    index = totalFreqs.index(maxFreq)
    freqsInOrder.append([chr(index + 97), maxFreq, 0])
    totalFreqs[index] = 0
    total += maxFreq
  totalProbs = 0
  for i in range(26):
    prob = freqsInOrder[i][1] * 1.0 / total
    prob *= 10000
    prob = int(round(prob,0))
    totalProbs += prob
    freqsInOrder[i][2] = prob
    print freqsInOrder[i]

buildWordIndex()
countFreqs()
generateProbs()
