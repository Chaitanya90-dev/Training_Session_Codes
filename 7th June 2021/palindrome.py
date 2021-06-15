# Program for Palindrome or not

user_input = input("Enter a number/string: ")

reversed_string = user_input[::-1]
print("Reversed user_input is: ",reversed_string)

if(user_input == reversed_string):
    print(user_input ," is a palindrome. Give me some more examples")
else:
    print(user_input, " is not a palindrome! Sorry try different like madam")
