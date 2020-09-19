
##Solve the Sudoku
def solve(board):
    
    #print_board(board)
    #print('______________________________________')
    
    empty_cell=find_empty_Cell(board)
    
    if not empty_cell:
        return True
    
    else:
        row,col=empty_cell
        
    #Fill the empty cell between 1 to 10 using backtracking algorithm
    for i in range(1,10):
        if is_valid_entry(board, i, (row,col)):
            board[row][col]=i
            
            if solve(board):
                return True
            
            board[row][col]=0
        
    return False


##Check if the number entered is valid or not
def is_valid_entry(board,num,pos):
    
    #Check Row
    for i in range(len(board[0])):
        if board[pos[0]][i]== num and pos[1]!=i:
            return False
        
    #Check Column
    for i in range(len(board)):
        if board[i][pos[1]]== num and pos[0]!=i:
            return False
    
    #Check Cube
    cube_x= pos[1] // 3
    cube_y= pos[0] // 3
    
    for i in range(cube_y * 3,cube_y * 3 + 3):
        for j in range(cube_x * 3, cube_x *3 +3):
            if board[i][j]== num and (i,j)!=pos:
                return False
    
    return True

## Find Empty Cell
def find_empty_Cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0 :
                return (i,j) #returning the empty cell as row,column
            
    return None


def print_board(board):
    
    for i in range(len(board)):
        if i%3==0 and i!=0 :
            print('------------------------')
        
        for j in range(len(board[0])):
            if j%3==0 and j!=0 :
                print(' | ',end='')
            if j==8 :
                print(board[i][j])
            else:
                print(str(board[i][j])+' ',end='')

##print_board(board)
##solve(board)
##print('___________________________________________________')
##print_board(board)