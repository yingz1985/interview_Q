#
# Complete the 'gridGame' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY grid
#  2. INTEGER k
#  3. STRING_ARRAY rules
#
#   For goldman sachs

#check neighbors and find value of alive
def gridGame(grid, k, rules):
    new_grid = []
    for iterations in range(k):    
        for i in range(len(grid)):
            new_grid.append([])
            for j in range(len(grid[i])):

                temp_val = getAliveNeighbors(grid,i,j)
                #new_grid[i].append(getAliveNeighbors(grid,i,j))
                if(rules[temp_val]=='alive'):
                    new_grid[i].append(1)
                else:

                    new_grid[i].append(0)
        grid = new_grid
        new_grid=[]

    return grid
                            


def getAliveNeighbors(grid,x,y):
    #at most 8 neighbors
    #[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y],[x+1,y+1],[x+1,y-1]
    #find sum of all alive neighbors, out of bound neighbors return 0
    
    neighbors = isAlive(grid,x-1,y-1)+isAlive(grid,x-1,y)+isAlive(grid,x-1,y+1)+isAlive(grid,x,y-1)+isAlive(grid,x,y+1)+isAlive(grid,x+1,y)+isAlive(grid,x+1,y+1)+isAlive(grid,x+1,y-1)
    return neighbors


def isAlive(grid,i,j):
  
    if(i<0 or i>=(len(grid)) or j<0 or j>=(len(grid[i]))): #out of bounds
        return 0
    else:
        print(i,j)
        return grid[i][j]

print(gridGame([[0,1,0,0],[0,0,0,0]],2,['dead','alive','dead','dead','dead','alive','dead','dead','dead']))


    
        
    
    
