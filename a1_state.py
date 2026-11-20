import copy

"""
Created on Mon Nov 16 15:13:04 2026
File: a1_state.py
Group number: A11
Student ID: 100539476, 100510450, 100539188
"""

class State:

    size = 5
    letters = [['A','B','C','D','E'],
               ['F','G','H','I','J'],
               ['K','L','M','N','O'],
               ['P','Q','R','S','T'],
               ['U','V','W','X','Y']]

    def __init__(self, grid):
        self.column = State.size
        self.row = State.size

        if grid is None:
            # empty board: 1 in every cell
            self.grid = [['1' for x in range(self.column)] for y in range(self.row)]
        else:
            assert(len(grid) == State.size)
            assert(len(grid[0]) == State.size)
            self.grid = [row[:] for row in grid] # copy of original

    def __str__(self):
        out = ''
        for row in self.grid:
            out += ' '.join(row) + '\n'
        return out

    def move(self, target):
        for x in range(State.size):
            for y in range(State.size):
                temp = s.letters[x][y]
                if temp == target:
                    print("index", x, y)
                    if s.grid[x][y] == '1':
                        s.grid[x][y] = '0'
                    else:
                        print("illegal move")  
                #else:
                    #print("not worked")
    def successors(self):
         futuregrid.grid = copy.deepcopy(s.grid)
         for x in range(State.size):
             for y in range(State.size):
                futuregrid.grid = copy.deepcopy(s.grid)
                if futuregrid.grid[x][y] == '1':
                    futuregrid.grid[x][y] = '0'
                    show(futuregrid)



def show(toprint):
    print("--Grid--")
    print(toprint)

s = State(None)
futuregrid = State(None)
show(s)
s.move("M")
show(s)
s.successors()
show(s)
