# Given a 2D integer array matrix, return the transpose of matrix.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
row,col=len(matrix),len(matrix[0])
transposed=[[0] *row for _ in range(col)] 
for i in range(row):
    for j in range(col):
        transposed[j][i]=matrix[i][j]
print(transposed)
#the above soultion  work on rectangular matrix 