def fill(mat,i,j):
    if(i==len(mat)-1 and j == len(mat)-1):
        return mat
    else:
        if mat[i][j] == 1:
            mat[i][j] = 2
            fill(mat,i-1,j-1) 
            fill(mat,i,j-1)
            fill(mat,i,j+1)    
def recursiv(num):
    if(num == 0):
        return
    print(num * num)
    return recursiv(num-1)
mat = [
    [1,1,0],
    [0,1,0],
    [1,0,1]
]
fill(mat,1,1)
print(f'{mat}\n')
recursiv(10)
# 1 == flood => 2 filled flood

