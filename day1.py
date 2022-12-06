file = open("./inputs/day1_input.txt", "r")
lineList = file.read().split('\n\n')
lineList = [x.replace('\n', ' ').split() for x in lineList]
file.close

# Part 1
def findCalsPerElf():
  calsDct = {}

  i = 0
  while i < len(lineList):
    groupSum = 0

    for num in lineList[i]:
      groupSum += int(num)

    calsDct[i] = groupSum
    
    i += 1
  
  return calsDct

def findMostCalories():
  calsPerElf = findCalsPerElf()

  return calsPerElf[max(calsPerElf, key=calsPerElf.get)]

print ('Part 1:', findMostCalories())
    

# Part 2
def findTop3CaloriesTotal():
  calsPerElf = findCalsPerElf()
  topElves = sorted(calsPerElf, key=calsPerElf.get, reverse=True)[:3]

  return calsPerElf[topElves[0]] + calsPerElf[topElves[1]] + calsPerElf[topElves[2]]


print ('Part 2:', findTop3CaloriesTotal())
