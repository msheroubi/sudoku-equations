import numpy as np
import sympy
from sudoku import Board

b = np.array([[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]).T

board = Board(b)

n = len(b)
        
# Rule of 45 | O(1)
r45 = n*(n+1) / 2

var = {}
R = {}
C = {}
theta = {}


equations = []

for x, y, val in board.Iterate():
    if val == 0:
        var[f'X{x}_{y}'] = sympy.symbols(f'X{x}_{y}')

for s in board.sqrs.values():
    eq = -r45
    for x, y, val in s.values:
        if val != 0:
            eq += val
        else:
            eq += var[f'X{x}_{y}']
    equations.append(eq)

for r in board.rows:
    eq = -r45
    for x, y, val in r.values:
        if val != 0:
            eq += val
        else:
            eq += var[f'X{x}_{y}']
    equations.append(eq)

for c in board.cols:
    eq = -r45
    for x, y, val in c.values:
        if val != 0:
            eq += val
        else:
            eq += var[f'X{x}_{y}']
    equations.append(eq)

for eq in equations:
    print(eq)