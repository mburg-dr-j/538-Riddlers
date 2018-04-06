def addGem (gemList, loc):
  global totalEV
  if loc == 0:
    newList = (gemList[0] + 1, gemList[1], gemList[2], gemList[3]*3)
  elif loc == 1:
    newList = (gemList[0], gemList[1] + 1, gemList[2], gemList[3]*2)
  else:
    newList = (gemList[0], gemList[1], gemList[2] + 1, gemList[3])
  if (0 in newList) and (sum(newList[0:3]) < 23):
    addGem (newList, 0)
    addGem (newList, 1)
    addGem (newList, 2)
  if (0 not in newList):
    totalEV += 1.0*newList[0]*newList[3]/6**sum(newList[0:3])
##    print newList[0:3], sum(newList[0:3]), 1.0*newList[0]*newList[3]/6**sum(newList[0:3])

totalEV = 0.0
addGem((0,0,0,1), 0)
addGem((0,0,0,1), 1)
addGem((0,0,0,1), 2)
print totalEV

