Q)Write a program to check whether given character is an alphabet ot not
---------------------------------------------------------------------------------------------
#Language used - python

ch = input("Please Enter a Character:  ")

# checking for alphabhet 
if(ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
    print(ch,"is a an alphabhet")
else:
    print(ch,"is not an alphabhet")

---------------------------------------------------------------------------------------------
#Output
Please Enter a Character:  A

A is a an alphabhet

Please Enter a Character:  r

r is a an alphabhet

Please Enter a Character:  }

} is not an alphabhet

Please Enter a Character:  "

" is not an alphabhet




