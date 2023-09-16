
def is_balanced(expression):
    brackets={
        ")":"(",
        "]":"[",
        "}":"{"
    }
    
    my_checked_expression=[]

    for char in expression:

        if char in "({[":
            my_checked_expression.append(char)
        elif char in ")]}":

            if not my_checked_expression or my_checked_expression.pop() != brackets[char]:
                return False

    
    return True

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1)) 
print(is_balanced(expression2)) 