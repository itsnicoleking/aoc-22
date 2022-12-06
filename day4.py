file = open("./inputs/day4_input.txt", "r")
lineList = [line.rstrip('\n').split(',') for line in file]
file.close

# Part 1
def isRangeSubset(range1, range2):
  return range1.start in range2 and range1[-1] in range2

def getNumContainingRanges():
  numContainedRanges = 0

  for line in lineList:
    rangeOneStart = int(line[0].split('-')[0])
    rangeOneEnd = int(line[0].split('-')[1])
    rangeTwoStart = int(line[1].split('-')[0])
    rangeTwoEnd = int(line[1].split('-')[1])

    rangeOne = range(rangeOneStart, rangeOneEnd+1)
    rangeTwo = range(rangeTwoStart, rangeTwoEnd+1)

    if isRangeSubset(rangeOne, rangeTwo) or isRangeSubset(rangeTwo, rangeOne):
      numContainedRanges += 1
  return numContainedRanges

print ('Part 1:', getNumContainingRanges())

# Part 2
def doesRangeOverlap(range1, range2):
  return range1.start in range2 or range1[-1] in range2

def getNumOverlappingRanges():
  numOverlappingRanges = 0

  for line in lineList:
    rangeOneStart = int(line[0].split('-')[0])
    rangeOneEnd = int(line[0].split('-')[1])
    rangeTwoStart = int(line[1].split('-')[0])
    rangeTwoEnd = int(line[1].split('-')[1])

    rangeOne = range(rangeOneStart, rangeOneEnd+1)
    rangeTwo = range(rangeTwoStart, rangeTwoEnd+1)

    if doesRangeOverlap(rangeOne, rangeTwo) or doesRangeOverlap(rangeTwo, rangeOne):
      numOverlappingRanges += 1
  return numOverlappingRanges

print ('Part 2:', getNumOverlappingRanges())
