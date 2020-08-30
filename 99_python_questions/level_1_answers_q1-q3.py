# To add or remove a block comment, do one of the following:
#      Highlight all code to block out.
#     Press Ctrl+/

#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000
# and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
single_line = []
single_line_append = single_line.append
for value in range(2000,3201):
    if value%7 == 0 and value&5 != 0:
        single_line_append(str(value))
print(", ".join(single_line))

#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program: 8
#Then, the output should be: 40320

factorial = 1
numb = []
numb_list = numb.append

# To take input from the user
num = int(input("Enter a number: "))

for i in range(1, num+1):
    factorial = factorial*i
    numb_list(str(factorial))
print(" ".join((numb)))
print("The factorial of ", num, "is ", factorial)

# Question 3
# Level 1
# # Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary. Suppose the following input is supplied to the program: 8
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()

num = int(input("Enter a number: "))
#create the dictionary
my_dict = {}
for i in range(1, num+1):
    my_dict[i] = i*i
print(my_dict)
