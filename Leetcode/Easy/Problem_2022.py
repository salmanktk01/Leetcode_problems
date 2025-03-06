# Convert 1D Array Into 2D Array
# Input: original = [1,2,3,4], m = 2, n = 2
# Output: [[1,2],[3,4]]
# Explanation: The constructed 2D array should contain 2 rows and 2 columns.
# The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
matrix=[1,2,3,4]
m=2
n=2
index=0
arr=[[0]*m for __ in range(n)]
print(arr)
for i in range(m):
    for j in range(n):
        arr[i][j]=matrix[index]
        index+=1
print("uzaor gando")
print(arr)