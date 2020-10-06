from algorithms.UninformedSearch import UninformedSearch
from algorithms.UninformedSearch import algorithms

actions = {
    'MOVEUP': 'move-up',
    'MOVEDOWN': 'move-down',
    'MOVELEFT': 'move-left',
    'MOVERIGHT': 'move-right'  
}

class SizeNPuzzle:
  def __init__(self, matrix):
    self.matrix = []

    for x in range(len(matrix)):
      self.matrix.append([])
      for y in range(len(matrix[x])):
        	self.matrix[x].append(matrix[x][y])
  
  def doAction(self, action):
    state = self.clone()
    i = 0
    j = None

    while (i < len(self.matrix)):
      m = self.findNone(self.matrix)
      j = m[1]
      i = m[0]
      if (j != -1):
        break

    #print("linha: ", i)
    #print("coluna: ", j)

    if (action == actions['MOVEDOWN']):
      state.matrix[i][j] = self.matrix[i + 1][j]
      state.matrix[i + 1][j] = None
    elif (action == actions['MOVEUP']):
      state.matrix[i][j] = self.matrix[i - 1][j]
      state.matrix[i - 1][j] = None
    elif (action == actions['MOVELEFT']):
      state.matrix[i][j] = self.matrix[i][j - 1]
      state.matrix[i][j - 1] = None
    elif (action == actions['MOVERIGHT']):
      state.matrix[i][j] = self.matrix[i][j + 1]
      state.matrix[i][j + 1] = None
    

    #print(state)
    return state


  def getActions(self):
    lista = []
    i = 0
    j = None

    #print(self.matrix)
    while (i < len(self.matrix)):
      m = self.findNone(self.matrix)
      j = m[1]
      i = m[0]
      if (j != -1):
        break

    #print("linha: ", i)
    #print("coluna: ", j)

    if (i + 1 < len(self.matrix)):
      lista.append(actions['MOVEDOWN'])
    
    if (i - 1 >= 0):
      lista.append(actions['MOVEUP'])

    if (j + 1 < len(self.matrix[i])):
      lista.append(actions['MOVERIGHT'])

    if (j - 1 >= 0):
      lista.append(actions['MOVELEFT'])

    return lista

  def equals(self, o):
    if (len(self.matrix) != len(o.matrix)):
      return False
    
    for i in range(len(self.matrix)):
      if (len(self.matrix[i]) != len(o.matrix[i])):
        return False
      
      for j in range(len(self.matrix[i])):
        if (self.matrix[i][j] != o.matrix[i][j]):
          return False
    
    return True

  def clone(self):
    return SizeNPuzzle(self.matrix)

  def __str__(self):
    str = "[\n"

    for i in range(len(self.matrix)):
      str += '[{}]\n'.format(self.matrix[i])
    
    str += "]"

    return str
  
  def findNone(self, lista):
    retorno = [-1, -1]
    idx = 0
    for element in lista:
      index = [i for i in range(len(element)) if element[i] == None]
      if(len(index) > 0):
        retorno = [idx, index[0]]
      
      idx += 1
    
    return retorno
  
initial = SizeNPuzzle(
    [
        [   4,    2,    7],
        [None,    8,    6],
        [   3,    5,    1]
    ]
)

finals = [
        SizeNPuzzle(
            [
                [   1,   4,   7],
                [   2,   5,   8],
                [   3,   6,None]
            ]
        )
    ]

problem = UninformedSearch(initial, finals)
result = problem.search(algorithms['DSF'])

if (result):
  for r in result:
    print(r)