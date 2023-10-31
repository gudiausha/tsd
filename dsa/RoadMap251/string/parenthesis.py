def minimumParentheses(pattern):

    # Write your code here
    # Return the minimum number of parentheses required.
    openbr = 0
    closebr = 0
    c = 0

    for i in pattern:
        if i == '(':
            openbr+=1
        else:
            closebr+=1
        
        if closebr>openbr:
            c = c+closebr-openbr
            closebr=0
            openbr=0
    
    c = openbr-closebr
    return c

    pass
