class TreeNode:
  def __init__(self, name, weight, parent):
    self.name = name
    self.weight = weight
    self.parent = parent
    self.children = []

  def __repr__(self):
    return self.name + ' ' + repr(self.weight)
  
  def printTree(self, level=0):
    print ('  ' * level + self.name + ' ' + repr(self.weight))
    for child in self.children:
      child.printTree(level+1)

  def getParent(self):
    return self.parent

  def addChild(self, node):
    if isinstance(node, TreeNode):
      self.children.append(node)
    else:
      print("Cannot add child - not a TreeNode")

  def getChildByName(self, name):
    for child in self.children:
      if child.name == name:
        return child

  def isLeaf(self):
    return not self.children

  def calculateWeight(self):
    if not self.isLeaf():
      for child in self.children:
        self.weight += child.calculateWeight()
      
    return self.weight

  def getAllFolders(self):
    if self.isLeaf():
      return []
    else:
      res = [self]
      for child in self.children:
        res += child.getAllFolders()

    return res

file = open("./inputs/day7_input.txt", "r")
lineList = [line.rstrip('\n') for line in file]
file.close

# Part 1
def parseTree():
  tree = TreeNode('/', 0, None)
  currentNode = tree

  for line in lineList:
    lineParts = line.split()
    # cmd
    if lineParts[0] == '$':
      # ignore root - already setup
      if lineParts[1] == 'cd' and lineParts[2] == '/':
        pass
      # cd
      elif lineParts[1] == 'cd':
        # up
        if lineParts[2] == '..':
          currentNode = currentNode.getParent()
        # down
        else:
          currentNode = currentNode.getChildByName(lineParts[2])
      # ignore ls
      elif lineParts[1] == 'ls':
        pass
    # dir
    elif lineParts[0] == 'dir':
      currentNode.addChild(TreeNode(lineParts[1], 0, currentNode))
    # file
    else:
      currentNode.addChild(TreeNode(lineParts[1], int(lineParts[0]), currentNode))
  
  tree.calculateWeight()
  return tree

def getSumFoldersMaxWeight100000():
  tree = parseTree()
  allFolders = [node.weight for node in tree.getAllFolders() if node.weight <= 100000]

  return sum(allFolders)

print ('Part 1:', getSumFoldersMaxWeight100000())

# Part 2
def getRootWeight(tree):
  allFolders = tree.getAllFolders()
  return int(str(allFolders[0]).split()[1])

def getSmallestDeletableFolderWeight():
  tree = parseTree()

  totalSpace = 70000000
  minRequiredSpace = 30000000
  currentFreeSpace = totalSpace - getRootWeight(tree)
  minDeletableFilesize = minRequiredSpace - currentFreeSpace

  smallestDeletableFolder = minRequiredSpace

  for folder in tree.getAllFolders():
    folderWeight = int(str(folder).split()[1])
    if folderWeight >= minDeletableFilesize and folderWeight <= smallestDeletableFolder:
      smallestDeletableFolder = folderWeight

  return smallestDeletableFolder

print ('Part 2:', getSmallestDeletableFolderWeight())
