# Reshape the Matrix
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
# we can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
#matrix koa reshape krna hae simple
mat = [[1,2],[3,4]]
n=len(mat)
r = 1
c = 4
one_matrix=[]
for i in range(len(mat)):
    for j in range(len(mat[0])):
       mat[i][j]=mat[n*i+j]
print(mat)