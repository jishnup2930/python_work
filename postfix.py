def evaluate(exp):
    stack = []
    for i in exp:
        if i == '+':
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(operand1+operand2)
        elif i == '-':
            stack.append(operand1-operand2)
        else:
            stack.append(int(i))
    return stack.pop()

