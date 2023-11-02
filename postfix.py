def evaluate(exp):
    stack = []
    operators = ['+', '-', '*', '/']
    
    for token in exp:
        if token not in operators:
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
    return stack.pop()
print(evaluate("22*"))

