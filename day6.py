from collections import Counter

file = open("./inputs/day6_input.txt", "r")
charList = list(file.read().rstrip('\n'))
file.close

# Part 1
def getMarkerStartPos(markerLen):
  i = markerLen-1
  while i < len(charList):
    markerArr = charList[i-(markerLen-1):i+1]
    duplicates = [k for k, v in Counter(markerArr).items() if v>1]

    if len(duplicates) == 0:
      return i+1

    i += 1

print ('Part 1:', getMarkerStartPos(4))

# Part 2
print ('Part 2:', getMarkerStartPos(14))
