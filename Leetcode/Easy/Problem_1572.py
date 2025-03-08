# Matrix Diagonal Sum
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
primary_diagonal = [mat[i][i] for i in range(len(mat))]

secondary_diagonal = [mat[i][len(mat)-1-i] for i in range(len(mat))]

total_sum = sum(primary_diagonal) + sum(secondary_diagonal)
#if the matrix is odd then the center element will be added twice so we need to subtract it 
if len(mat) % 2 == 1:  
    center = mat[len(mat)//2][len(mat)//2]
    total_sum -= center
print(total_sum)