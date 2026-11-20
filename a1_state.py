# Very important, do not remove or else both successors and futuresight break.
import copy
import random

"""
Created on Mon Nov 16 15:13:04 2026
File: a1_state.py
Group number: A11
Student ID: 100539476, 100510450, 100539188
"""

# Robert here, im going to try adding notes to whatever code I changed / added to make it clear what it does.

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

    # Move now takes a target.
    def move(self, target):
        for x in range(State.size):
            for y in range(State.size):
                temp = s.letters[x][y]
                if temp == target:
                    print("index", x, y)
                    if s.grid[x][y] == '1':
                        s.grid[x][y] = '0'
                        movecost(s, x, y)
                    else:
                        print("illegal move")  
                #else:
                    #print("not worked")



    # Successors can output all potential reachable gamestates with 1 move.
    def successors(self):
         futuregrid.grid = copy.deepcopy(s.grid)
         for x in range(State.size):
             for y in range(State.size):
                futuregrid.grid = copy.deepcopy(s.grid)
                if futuregrid.grid[x][y] == '1':
                    futuregrid.grid[x][y] = '0'
                    #show(futuregrid)


    # Returns the "best" (the cheapest) move currently possible. 
    # Does not currently account for points gained from hingers.
    def futuresight(self):
             futuregrid.grid = copy.deepcopy(s.grid)
             runningcost = 100
             costofmove = 0
             agoodmove = State(None)
             for x in range(State.size):
                 for y in range(State.size):
                    futuregrid.grid = copy.deepcopy(s.grid)
                    if futuregrid.grid[x][y] == '1':
                        futuregrid.grid[x][y] = '0'
                        costofmove = movecost(futuregrid, x, y)
                        # Lazy version of adding variance to the prediction code for when two moves have equal cost/reward.
                        # Probably should be replaced by some more advanced version in the actual AI code.
                        if runningcost == costofmove:
                            if random.random() > 0.7:
                                runningcost = copy.deepcopy(costofmove)
                                agoodmove.grid = copy.deepcopy(futuregrid.grid)
                        if runningcost > costofmove:
                            runningcost = copy.deepcopy(costofmove)
                            agoodmove.grid = copy.deepcopy(futuregrid.grid)
             return agoodmove
    



# Returns the cost of a move on the given board. Works on corner / edge tiles.
def movecost(self, xcord, ycord):
    xcheck = 2
    ycheck = 2
    xstart = -1
    ystart = -1
    runningcost = 0
    if(xcord == 0):
        xstart = 0
    if(ycord == 0):
        ystart = 0
    if(xcord == 4):
       xcheck = 1
    if(ycord == 4):
        ycheck = 1
    for x in range(xstart, xcheck):
        for y in range(ystart, ycheck):
            runningcost = runningcost + int(self.grid[x+xcord][y+ycord])
    return runningcost

    

# Now needs a grid to be given as an input.
def show(toprint):
    print("--Grid--")
    print(toprint)


# Allows a set of positions to be turned into a letter for the "move" function to use.
def translator(self, xcord, ycord):
    for x in range(State.size):
                for y in range(State.size):
                    temp = s.letters[x][y]
                    if x == xcord and y == ycord:
                        return s.letters[x][y]
                        

s = State(None)
futuregrid = State(None)
show(s)
s.move("M")
show(s)
s.successors()
show(s.futuresight())
#show(s)



    




