Q)Write a program to print all perfect numbers between 1 to n.
--------------------------------------------------------------------------------
#Language used - python

lower_limit = int(input("Enter a Lower limit of range: "))
upper_limit = int(input("Enter a upper limit of range: "))

for num in range(lower_limit,upper_limit+1):
    sum = 0
    for i in range(1,num):
        if(num%i) == 0:
            sum = sum+i
        
    if(num==sum):
        print(num)
       

-----------------------------------------------------------------------------------
#Output

Enter a upper limit of range: 500

6

28

496

Enter a Lower limit of range: 1

Enter a upper limit of range: 10

6










