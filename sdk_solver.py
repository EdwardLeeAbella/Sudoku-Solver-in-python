# sudoku solver with back track algo

# steps 

# 1. Pick an empty position or squre in the sudoku board
# 2. Try all num in range from 1 to 9
# 3. Find if its valid by traversing through the matrix or sudoku board
# 4. Repeat
# 5. Backtrack to the last position

sudoku_board = [
    [0,2,3,0,1,0,0,7,0],
    [0,7,0,0,2,6,0,0,0],
    [0,0,9,0,0,0,0,0,0],
    [2,4,0,0,3,1,5,0,6],
    [0,0,0,4,0,8,0,0,0],
    [0,0,0,0,6,0,3,4,0],
    [5,6,2,0,0,3,0,0,0],
    [0,1,0,0,7,0,0,0,0],
    [0,0,0,0,5,4,6,0,0]
]

def solve(bo):

    #print(bo) #printing step by step solution

    find = find_empty(bo)
    if not find:
        return True # means that we complete the solution
    else:
        i, j = find

    for row in range(1, 10):
        if valid(bo, row, (i, j)):
            bo[i][j] = row
            if solve(bo):
                return True
            bo[i][j] = 0

    return False

def valid(bo, num, pos):
    #check row
    for row in range(len(bo[0])):
        if bo[pos[0]][row] == num and pos[1] !=0: #checking each element in row if theres a same num value
            return False
    #check column
    for row in range(len(bo)):
        if bo[row][pos[1]] == num and pos[0] != 0: #checking each element in col if theres a same num value 
            return False
    #Check box or cube of 3x3
    cube_row = pos[1] // 3  #setting up the position
    cube_col = pos[0] // 3  #setting up the position

    for row in range(cube_col*3, cube_col*3 + 3):
        for col in range(cube_row*3, cube_row*3 + 3):
            if bo[row][col] == num and (row, col) != pos: #checking if the num has the same value in the current cube 
                return False

    return True # if we traverse in the row,col, and cube and does not find any same num value return True

def print_board(bo):

     for row in range(len(sudoku_board)):
        if row % 3 == 0 and row != 0: #checking if row is divisible by 3 
            print("- - - - - - - - - - - - ")

        for col in range(len(bo[0])):
            if col % 3 == 0 and col != 0:#checking if each position is divisible by 3 
                print(" | ", end="")

            if col == 8: # if column in the last position
                print(bo[row][col])
            else:
                print(str(bo[row][col]) + " ", end="")
#print_board(sudoku_board)

def find_empty(bo): # find empty value in the board 

    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return (row, col)  # row, col
    return None

    
print("Sudoku Board ")
print()
print_board(sudoku_board)
solve(sudoku_board)
print("Answer :")
print()
print_board(sudoku_board)

