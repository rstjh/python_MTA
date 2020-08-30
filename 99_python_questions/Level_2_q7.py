# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1, Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
# Hints:
# Note: In case of input data being supplied to the question,
# it should be assumed to be a console input in a comma-separated form.


matrix = (input( "Enter the row size and column size seperated by a comma. " ).split( "," ))
#print(matrix)
row_num = int(matrix[0])
col_num = int(matrix[1])

multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

#print((row_num).strip(" "))
#print((col_num).strip(" "))
for row in range(int(row_num)):
    for col in range(int(col_num)):
        multi_list[row][col]= row*col
print(multi_list)
