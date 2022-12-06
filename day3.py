import string

file = open("./inputs/day3_input.txt", "r")
lineList = [line.rstrip('\n') for line in file]
file.close

priorities = dict.fromkeys(x for x in string.ascii_letters)
priorities.update((k, i) for i, k in enumerate(priorities, start=1))

# Part 1
def getAllIntersects():
  intersections = []

  for line in lineList:
    firstCompartment = list(line[:len(line)//2])
    secondCompartment = list(line[len(line)//2:])

    intersections.extend(list(set(firstCompartment).intersection(secondCompartment)))

  return intersections

def getSumIntersectsPriorities(intersectsList):
  priorityTotal = 0

  for intersect in intersectsList:
    priorityTotal += priorities[intersect]
  
  return priorityTotal

print ('Part 1:', getSumIntersectsPriorities(getAllIntersects()))

# Part 2
def getGroupOfThreeIntersects():
  intersections = []

  i = 0
  while i < len(lineList)/3:
    elfOne = lineList[i*3]
    elfTwo = lineList[i*3+1]
    elfThree = lineList[i*3+2]

    intersections.extend(list(set(elfOne) & set(elfTwo) & set(elfThree)))

    i += 1
  
  return intersections

print ('Part 2:', getSumIntersectsPriorities(getGroupOfThreeIntersects()))
