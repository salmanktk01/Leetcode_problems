# Reshape the Matrix
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
# we can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
#matrix koa reshape krna hae simple
mat = [[1,2],[3,4]]
n=len(mat)
r = 1
c = 4
if len(mat) * len(mat[0]) != r * c:
            print("not possible reshape")
new_mat=[[0]*c for _ in range(r)] #Rows x Column (r x c )
print(new_mat) #the matrix we need to create but the values with the the above matrix 
idx = 0
        # Traverse the matrix through the loop... 
while idx < r * c:
            # idx % c will give us the current column number...
            # idx / c will give us how many rows we have completely filled...
            new_mat[idx // c][idx % c] = mat[idx // len(mat[0])][idx % len(mat[0])]
            idx += 1
print(new_mat)