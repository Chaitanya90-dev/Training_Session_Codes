Q)Write a program to count the number of digits in a given interger
------------------------------------------------------------------------------------
#Language used - python

n = int(input("Enter a number: "))
count = 0

#Checking digits in number 
while(n>0):
    n = n//10
    print("n is: ",n)
    count = count + 1
    print("count is: ",count)

print("Total Number of Digits in Number are: ",count)

---------------------------------------------------------------------------------
#Output
Enter a number: 789789789789

n is:  78978978978

count is:  1

n is:  7897897897

count is:  2

n is:  789789789

count is:  3

n is:  78978978

count is:  4

n is:  7897897

count is:  5

n is:  789789

count is:  6

n is:  78978

count is:  7

n is:  7897

count is:  8

n is:  789

count is:  9

n is:  78

count is:  10

n is:  7

count is:  11

n is:  0

count is:  12

Total Number of Digits in Number are:  12




    
