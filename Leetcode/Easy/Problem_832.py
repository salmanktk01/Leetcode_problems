# Flipping an Image
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
image = [[1,1,0],[1,0,1],[0,0,0]]
flipped=[row[::-1] for row in image]
for row in range(len(flipped)):
    for column in range(len(flipped[0])):
        if(flipped[row][column]==1):
            flipped[row][column]=0
        else:
            flipped[row][column]=1
print(flipped)