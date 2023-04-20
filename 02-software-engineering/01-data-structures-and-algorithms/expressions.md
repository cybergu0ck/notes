# Infix expressions

* Infix notation is how expressions are written and recognised by humans and is generally how expressions are entered in programs.
* The opertor is placed between the two operands.
* Example: a+b/c-d

<br>
<br>

# Postfix expressions

* Computers uses postfix notation to evaluate expressions.
* Every operator follows all its operands.
* Example: abc/+d-

<br>
<br>

# Conversion of infix to postfix expression

* stack is used to convert an infix expression to postfix expression.
    ```python
    def to_post_fix(in_fix_expression):
        """Convert infix to postfix"""
        in_fix_expression = in_fix_expression.replace(" ",'')       #Remove all whitespace
        post_fix_expression = ""
        stack = []
        operator_precedence = {'^':1, '/':2, '*':2, '+':3, '-':3}   #lower the 'value' higher the priority for the 'key'

        for i in in_fix_expression:
            if i not in operator_precedence and i != '(' and i != ")":
                post_fix_expression += i
            
            elif i == '(':
                stack.append(i)
            
            elif i == ')':
                while stack:
                    popped = stack.pop()
                    if popped == '(':
                        break
                    else:
                        post_fix_expression += popped

            elif i in operator_precedence:
                if stack:
                    if stack[-1] == '(':
                        stack.append(i)
                    
                    elif operator_precedence[stack[-1]] <= operator_precedence[i]:
                        while stack:
                            if stack[-1] == '(':
                                stack.append(i)
                                break
                            if operator_precedence[stack[-1]] > operator_precedence[i]:
                                stack.append(i)
                                break
                            elif operator_precedence[stack[-1]] <= operator_precedence[i]:
                                post_fix_expression += stack.pop()
                        else:     #The code in this else block is executed only if the while loop terminates without the break statement!
                            stack.append(i)
                    elif operator_precedence[stack[-1]] > operator_precedence[i]:
                        stack.append(i)

                else:
                    stack.append(i)  
        while stack:
            post_fix_expression += stack.pop()

        return post_fix_expression



    print(to_post_fix("a + b*(c^d-e)^(f+g*h)-i"))

    #>abcd^e-fgh*+^*+i-
    ```

* Watch this [video](https://external.ink?to=//www.youtube.com/watch?v=kKSENzdu7bE&list=PL1XjRDnU2tOjIgT7L1pzc-un9M78SkcWh&index=50 ) to understand the logic in converting infix expression to postfix expression.

* Watch this [video](https://external.ink?to=//www.youtube.com/watch?v=ymG0zxuC__I) to code the function to convert infix to postfix expression (where '^' and '(' ')' are included.)

