Q)Find total occurrences of each digits (0-9) using function.
-----------------------------------------------------------------------------
#Language used - python

number=int(input("Enter any Number: "))
print("Digit\tFrequency")

def countOccurrances(number):
    
    for i in range(0,10):
        
        count=0;
        temp=number;
        
        while temp>0:
            
            digit=temp%10
            
            if digit==i:
                count=count+1
                
            temp=temp//10;
            
        if count>0:
            print(i,"\t",count)
        
countOccurrances(number)
----------------------------------------------------------------------------
#Output

Enter any Number: 12345664558859963321147889665422

Digit	Frequency

1 	 3

2 	 4

3 	 3

4 	 4

5 	 5

6 	 5

7 	 1

8 	 4

9 	 3



