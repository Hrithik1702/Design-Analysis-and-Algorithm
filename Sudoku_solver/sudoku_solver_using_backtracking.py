import copy as c

l=[[3,0,9,0,0,0,2,0,1],
  [0,0,2,8,0,0,0,0,0],
  [4,0,0,0,3,0,0,7,5],
  [0,0,0,4,0,8,0,2,9],
  [5,0,0,0,0,0,7,0,0],
  [0,0,4,0,2,7,0,0,0],
  [0,7,6,5,8,3,4,0,2],
  [0,4,3,0,1,2,9,5,6],
  [0,1,5,9,0,0,0,0,0]]

            
def sudoku_solver(row,col,l):
    nl = c.deepcopy(l)
    print("row=",row," ","col = ",col)
    if(nl[row][col] != 0):
        print("Non zero element")
        if(col == 8):
            if(row == 8):
                print("*****")
                print_list(l)
                return l
            else:
                sudoku_solver(row+1,0,nl)
        else:
            sudoku_solver(row,col+1,nl)
    else:
        print("row=",row," ","col = ",col)
        for value in range(1,10):
            if(possible(value,row,col,nl)):
                print("possible(",value,",",row,",",col,")")
                nl[row][col] = value
                if(col == 8):
                    if(row == 8):
                        print("*****")
                        print_list(nl)
                        return nl
                    else:
                        sudoku_solver(row+1,0,nl)
                else:
                    sudoku_solver(row,col+1,nl)
        print("BackTacking - ","row=",row,"col=",col)


def possible(value,row,col,l):
    #checking in the same row
    for i in range(0,9):
        if value == l[i][col]:
            return False
    #checking in the same col
    for i in range(0,9):
        if value == l[row][i]:
            return False
    #finding the square's first element
    r = (row//3) * 3
    c = (col//3) * 3
    #checking in the same square
    for i in range(r,r+3):
        for j in range(c,c+3):
            if value == l[i][j]:
                return False
    return True

def print_list(l):
    for i in l:
        print()
        for j in i:
            print(j,end=" ")

rl = sudoku_solver(0,0,l)



        
        


                
            
                    
