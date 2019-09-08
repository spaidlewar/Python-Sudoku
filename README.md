# Python-Sudoku
This is a simple Python Based Sudoku Generator and Solver that uses a recursive back tracking algorithm to solve sudoku puzzles.
Sudoku is a popular number puzzle that requires you to fill blanks in a 9X9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids contains all of the digits from 1 to 9.
## Requirements:
1.Python 3.6 or above

2.Random Module

## Usage:
### To generate a Sudoku Puzzle and Solve the Same
1. Create an object of class Sudoku() 
2. Call the sudoku_generator() method on this object and store it in a variable.
3. To print the generated sudoku, call the print_grid() method 
   on the sudoku object and pass the variable used in step 2.
4. To solve this Generated Sudoku Puzzle, Call the sudoku_solver() method
   on the object and pass the variable used in step 2.
5. To print the solved sudoku, call the print_grid() method 
   on the sudoku object and pass the variable used in step 2.  
   
#### Example Code:
mySudoku = Sudoku()

sudoku_grid = mySudoku.sudoku_generator()

mySudoku.print_grid(sudoku_grid)

mySudoku.sudoku_solver(sudoku_grid)

mySudoku.print_grid(sudoku_grid)
   
### To Solve a User Desired Sudoku Puzzle
1. Create manually a list of list of 9 row elements of desired sudoku.
2. Create an object of class Sudoku()
3. Call the sudoku_solver() method on the object and pass the sudoku_grid you created

#### Example Code:
my_grid = [

            [0,0,0,0,0,5,0,0,0],

            [0,5,0,0,0,0,0,8,0],
            
            [2,0,4,0,0,8,0,0,1],
            
            [4,0,0,0,1,0,8,0,7],
            
            [0,0,0,0,5,2,0,0,6],
            
            [6,0,0,8,0,0,0,2,5],
            
            [0,0,0,0,0,0,5,0,0],
            
            [7,4,2,0,9,0,1,6,0],
            
            [0,9,0,0,0,0,0,0,0]
           ]
            
            
mySudoku = Sudoku()

mySudoku.sudoku_solver(my_grid)

mySudoku.print_grid(my_grid)


## References:

Backtracking Algorithm using recursion for sudoku: https://codepumpkin.com/sudoku-solver-using-backtracking/

Algorithm for generating a sudoku: https://www.geeksforgeeks.org/program-sudoku-generator/ 


Other References: https://www.technologyreview.com/s/426554/mathematicians-solve-minimum-sudoku-problem/
