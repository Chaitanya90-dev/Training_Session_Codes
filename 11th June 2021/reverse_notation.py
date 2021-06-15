operators = set(['+', '-', '*', '/', '(', ')', '^'])  

priority = {'+':1, '-':1, '*':2, '/':2, '^':3}  

 
def infix_to_postfix(expression): 

    stack = [] 

    output = ''

    

    for ch in expression:

        if ch not in operators: #operand ahe 

            output+= ch  #then put it into output 

        elif ch=='(':  # else operators should be put in stack

            stack.append('(')  #left bracket asel tr stack mdhe taka

        elif ch==')':   #  joparyant ( milat nhi toparyant scan kra and tya chya agoder je pn yetil te pop kra

            while stack and stack[-1]!= '(':

                output+=stack.pop()  

            stack.pop()

        else:

            # lesser priority can't be on top on higher or equal priority    

             # so pop and put in output   

            while stack and stack[-1]!= '(' and priority[ch]<=priority[stack[-1]]:

                output+=stack.pop()

            stack.append(ch)

    while stack:

        output+=stack.pop()

    return output

 

expression = str(input('Enter infix expression'))

print('infix expression: ',expression)

print('postfix expression: ',infix_to_postfix(expression))


# POSTFIX EVALUTION 


# If user wants to type input
# expression = str(input('Enter infix expression'))

def eval_expression(arr):
    stack = []
    operator = ["+","-","*","/","%"]

    for item in arr:
        # check for operand 
        if item not in operator:
            stack.append((item))
            
        # check for operator
        else:
            first = int(stack.pop())
            second = int(stack.pop())

            if(item == "+"):
                stack.append(second + first)

            if(item == "-"):
                stack.append(second - first)

            if(item == "*"):
                stack.append(second * first)

            if(item == "/"):
                stack.append(second + first)

            if(item == "%"):
                stack.append(second % first)

    return stack[-1]

a = ["5","6","2","3","*"]
print(eval_expression(a))
            