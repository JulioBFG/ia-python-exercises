import UninformedSearch, algorithms

class actions:
    MOVEUP: 'move-up',
    MOVEDOWN: 'move-down',
    MOVELEFT: 'move-left',
    MOVERIGHT: 'move-right'  

class SizeNPuzzle:
    def __init__ (matrix):
        self.matrix = []

        for ( i = 0 i < matrix.length i++) {
            self.matrix.push([... matrix[i]])
        }
    

    def doAction(action):
        state = self.clone()
        i,j 

        #REVER FOR
        for i in self.matrix.length:
            j = self.matrix[i].index()
                
            if (j != -1):
                break

            +1

        if (action == actions.MOVEDOWN):
            state.matrix[i][j] = self.matrix[i + 1][j]
            state.matrix[i + 1][j] = null
        elif (action == actions.MOVEUP):
            state.matrix[i][j] = self.matrix[i - 1][j]
            state.matrix[i - 1][j] = null
        elif (action == actions.MOVELEFT):
            state.matrix[i][j] = self.matrix[i][j - 1]
            state.matrix[i][j - 1] = null
        elif (action == actions.MOVERIGHT):
            state.matrix[i][j] = self.matrix[i][j + 1]
            state.matrix[i][j + 1] = null

        return state
    

    def getActions():
         list = []

         i,j

         #REVER FOR
        for (i = 0 i < self.matrix.length i++) {
            j = self.matrix[i].findIndex(value => !value)
            
            if (j != -1) {
                break
            }
        }

        if (i + 1 < self.matrix.length):
            list.push(actions.MOVEDOWN)

        if (i - 1 >= 0):
            list.push(actions.MOVEUP)

        if (j + 1 < self.matrix[i].length):
            list.push(actions.MOVERIGHT)

        if (j - 1 >= 0):
            list.push(actions.MOVELEFT)

        return list

    def equals(o):
        if (self.matrix.length != o.matrix.length):
            return false

        for ( i = 0 i < self.matrix.length i++):
            if (self.matrix[i].length != o.matrix[i].length):
                return false
            
            for ( j = 0 j < self.matrix[i].length j++):
                if (self.matrix[i][j] != o.matrix[i][j]):
                    return false

        return true

    def clone():
        return SizeNPuzzle(self.matrix)

    def toString():
         str = "[\n"
        
        for ( i = 0 i < self.matrix.length i++):
            str += f"[${self.matrix[i]}]"

        str += "]"
        return str


initial = SizeNPuzzle(
    [
        [   4,    2,    7],
        [null,    8,    6],
        [   3,    5,    1]
    ]
)

finals = [
    SizeNPuzzle(
        [
            [   1,   4,   7],
            [   2,   5,   8],
            [   3,   6,null]
        ]
    )
]

problem = UninformedSearch(initial, finals)

result = problem.search() 

if (result):
    for state in result:
        print(state.toString())
