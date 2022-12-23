# sudoku-equations
Convert a sudoku board from an NP array into a system of equations

### Requirements
Needs Python version > 3.9

```
numpy
sympy
```

### Usage
Given a sudoku board of size N as an numpy array:


Inside sudoku-equations.py, update "b"
```
b = np.array([[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]).T
```

Convert board into a system of equations. Number of equations = n * 3; An equation for every row, column and square.

#### Sample Output:
```
X0_2 + X1_1 + X2_0 + X2_1 - 14.0
X1_3 + X1_4 + X1_5 + X2_3 + X2_4 + X2_5 - 26.0
X0_6 + X0_7 + X0_8 + X1_7 + X1_8 + X2_6 + X2_7 + X2_8 - 39.0
X3_0 + X3_2 + X4_2 + X5_0 + X5_2 - 23.0
X3_3 + X3_5 + X4_4 + X5_3 + X5_5 - 26.0
X3_6 + X3_8 + X4_6 + X5_6 + X5_8 - 23.0
X6_0 + X6_1 + X6_2 + X7_0 + X7_1 + X8_0 + X8_1 + X8_2 - 39.0
X6_3 + X6_4 + X6_5 + X7_3 + X7_4 + X7_5 - 35.0
X6_7 + X6_8 + X7_7 + X8_6 - 14.0
X2_0 + X3_0 + X5_0 + X6_0 + X7_0 + X8_0 - 30.0
X1_1 + X2_1 + X6_1 + X7_1 + X8_1 - 24.0
X0_2 + X3_2 + X4_2 + X5_2 + X6_2 + X8_2 - 22.0
X1_3 + X2_3 + X3_3 + X5_3 + X6_3 + X7_3 - 28.0
X1_4 + X2_4 + X4_4 + X6_4 + X7_4 - 29.0
X1_5 + X2_5 + X3_5 + X5_5 + X6_5 + X7_5 - 30.0
X0_6 + X2_6 + X3_6 + X4_6 + X5_6 + X8_6 - 29.0
X0_7 + X1_7 + X2_7 + X6_7 + X7_7 - 26.0
X0_8 + X1_8 + X2_8 + X3_8 + X5_8 + X6_8 - 21.0
X0_2 + X0_6 + X0_7 + X0_8 - 15.0
X1_1 + X1_3 + X1_4 + X1_5 + X1_7 + X1_8 - 27.0
X2_0 + X2_1 + X2_3 + X2_4 + X2_5 + X2_6 + X2_7 + X2_8 - 37.0
X3_0 + X3_2 + X3_3 + X3_5 + X3_6 + X3_8 - 32.0
X4_2 + X4_4 + X4_6 - 12.0
X5_0 + X5_2 + X5_3 + X5_5 + X5_6 + X5_8 - 28.0
X6_0 + X6_1 + X6_2 + X6_3 + X6_4 + X6_5 + X6_7 + X6_8 - 43.0
X7_0 + X7_1 + X7_3 + X7_4 + X7_5 + X7_7 - 24.0
X8_0 + X8_1 + X8_2 + X8_6 - 21.0

```
