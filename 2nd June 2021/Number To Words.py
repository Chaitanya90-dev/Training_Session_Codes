# program to print number to words 

from typing import final


n = int(input("enter a number you want to convert it into words: "))

highers = ["lakhs crores","lakh crore","Hundred crores","Hundred crore","crores","crore","lakhs","lakh","thousands",
            "thousand","hundred","hundred and"]

tens = [" "," ","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

units = [" ","one","two","three","four","five","six","seven","eight","nine","ten",
            "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

lakhCrores = ((n//100000000000)%100)

hundredCrores = ((n//1000000000)%100)

crore = ((n//10000000)%100)

lakh = ((n//100000)%100)

thousand = ((n//1000)%100)

hundred = ((n//100)%10)

ten = (n%100)

final_word =""  


print(lakhCrores)
print(hundredCrores)
print(crore)
print(lakh)
print(thousand)
print(hundred)
print(ten)


if(lakhCrores > 0):
    if(lakhCrores > 9 and lakhCrores <= 19):
        final_word = final_word + " " + units[lakhCrores] + " " + highers[0]

    elif(lakhCrores > 19):
        final_word = final_word + " " + tens[lakhCrores//10] + " " + units[lakhCrores%10] + " " + highers[0]
    
    else:
        final_word = final_word + " " + units[lakhCrores] + " " + highers[1]
        

if(hundredCrores > 0):
    if(hundredCrores > 9 and hundredCrores <= 19):
        final_word = final_word + " " + units[hundredCrores] + " " + highers[2]
    
    elif(hundredCrores > 19):
        final_word = final_word + " " + tens[hundredCrores//10] + " " + units[hundredCrores%10] + " " + highers[2]

    else:
        final_word = final_word + " " + units[hundredCrores] + " " + highers[3]

if(crore > 0):
    if(crore > 9 and crore <= 19):
        final_word = final_word + " " + units[crore] + " " + highers[4]
    
    elif(crore > 19):
        final_word = final_word + " " + tens[crore//10] + " " + units[crore%10] + " " + highers[4]

    else:
        final_word = final_word + " " + units[crore] + " " + highers[5]


if(lakh > 0):
    if(lakh > 9 and lakh <= 19):
        final_word = final_word + " " + units[lakh] + " " + highers[6]
    
    elif(lakh > 19):
        final_word = final_word + " " + tens[lakh//10] + " " + units[lakh%10] + " " + highers[6]

    else:
        final_word = final_word + " " + units[lakh%10] + " " + highers[7]


if(thousand > 0):
    if(thousand > 9 and thousand <= 19):
        final_word = final_word + " " + units[thousand] + " " + highers[8]
    
    elif(thousand > 19):
        final_word = final_word + " " + tens[thousand//10] + " " + units[thousand%10] + " " + highers[8]

    else:
        final_word = final_word + " " + units[thousand%10] + " " + highers[9]


if(hundred > 0):
    if((hundred//100)):
        final_word = final_word + " " + units[hundred%10] + " " + highers[10]

    else:
        final_word = final_word + " " + units[hundred%10] + " " + highers[11]

if(ten > 19):
    final_word = final_word + " " + tens[ten//10] + " " + units[ten%10]

else:
    final_word = final_word + " " +units[ten]


if(n==0):
    final_word = "Zero"


print("final words is: ", final_word)