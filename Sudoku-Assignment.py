#!/usr/bin/env python
# coding: utf-8



import random

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(str(grid[i][j]) + ' ',end = '')
        print('')
def find_empty_location(grid,location): 
    '''Finds empty location in the grid passed to it and stores it's row and column in location list '''
    for row in range(9): 
        for col in range(9): 
            if(grid[row][col]==0): 
                location[0]=row 
                location[1]=col 
                return True
    return False
  
def in_row(grid,row,num): 
    '''Checks if a number occurs in the row'''
    for i in range(9): 
        if(grid[row][i] == num): 
            return True
    return False
  
def in_col(grid,col,num): 
    '''Checks if a number occurs in the column'''
    for i in range(9): 
        if(grid[i][col] == num): 
            return True
    return False
  
def in_box(grid,row,col,num): 
    '''Checks if a number is in the 3x3 box'''
    row = row - row%3
    col = col - col%3
    for i in range(3): 
        for j in range(3): 
            if(grid[i+row][j+col] == num): 
                return True
    return False
  
def is_allowed(grid,row,col,num):  
    '''Checks if a number is allowed in given position with passed row number and column using above functions'''
    if(in_row(grid,row,num) or in_col(grid,col,num) or in_box(grid,row,col,num)):
        return False
    else:
        return True
    
def sudoku_solver(grid): 
    '''This Function uses above defined functions to check various condition to implement a backtracking algorithm.
    It takes in an input 'grid' and assigns values to each empty location to see if it reaches a solution. '''    
    # Start from top left spot and recursively find empty locations to try placing digits 
    location=[0,0] 
    original_grid = grid[:]
    # We assign a number only if it meets the conditions so 
    #If all locations are filled,i.e find_empty_location returns False
    #sudoku is solved and we return True(recursion base condition).   
    if(not find_empty_location(grid,location)): 
        return True
      
    # Assigning location row and col the values of empty location that we got from above function.  
    row=location[0] 
    col=location[1] 
      
    # We try all digits from 1-9.
    for num in range(1,10): 
          
        # If digit is allowed we proceed  
        if(is_allowed(grid,row,col,num)): 
              
            # assign allowed number temporarily to see if it leads to a solution
            grid[row][col]=num 
  
            # If we reach a solution for given set of number, i.e all locations are filled, 
            # (we reach recursion base condition) we return True.
            if(sudoku_solver(grid)): 
                return True
  
            # if we don't find solution, remove assigned number & try again for next number
            grid[row][col] = 0
              
    # We don't find a solution and hence return False         
    return False



def fill_box(grid,row,col): 
    '''Checks if a number is in the 3x3 box'''
    box_nums = []
    while(len(box_nums) < 9):
        num = random.randint(1,9)
        if num not in box_nums:
            box_nums.append(num)
    row = row - row%3
    col = col - col%3
    num_index = 0
    for i in range(3): 
        for j in range(3): 
            grid[i+row][j+col] = box_nums[num_index]
            num_index += 1

def sudoku_generator():
    '''This function generates a sudoku grid in the form of and returns the grid in list of list of row elements'''
    grid_generate = [[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0]]
    
    # First we fill all the diagonal 3x3 matrices since they are independent of adjacent matrices
    fill_box(grid_generate,0,0)
    fill_box(grid_generate,3,3)
    fill_box(grid_generate,6,6)
    
    # Now we solve the partially filled sudoku with our sudoku solver to generate a fully solved sudoku grid
    sudoku_solver(grid_generate)
    
    # Now we will remove random elements from the sudoku grid generated above to create a sudoku puzzle
    
    # we make a list of all locations and shuffle it randomly to maintain randomness of deletion of elements
    location_list = [[row,col] for row in range(0,9) for col in range(0,9)]
    random.shuffle(location_list)
    to_del = location_list[15:70]
    
    # we delete 55 elements from the sudoku grid to give a sudoku puzzle with 21 clues. Since the chances of a
    # unique solutin are higher with atleast 18 clues.
    for location in to_del:
        row = location[0]
        col = location[1]
        grid_generate[row][col] = 0
    
    return grid_generate

################################################################################################################
'''Testing Code for our Sudoku Generator and Solver'''
grid_generate = sudoku_generator()
grid = grid_generate[:]
print("Generated Sudoku Puzzle:")
print_grid(grid_generate)
print('')
if(sudoku_solver(grid)):
    print("Solution for Sudoku:")
    print_grid(grid)
else:
    print('No Solution exists for Given Puzzle')


# References:
# 
# Backtracking Algorithm using recursion for sudoku: https://codepumpkin.com/sudoku-solver-using-backtracking/
# 
# Algorithm for generating a sudoku: https://www.geeksforgeeks.org/program-sudoku-generator/ 
# 
# 
# Other References: https://www.technologyreview.com/s/426554/mathematicians-solve-minimum-sudoku-problem/
