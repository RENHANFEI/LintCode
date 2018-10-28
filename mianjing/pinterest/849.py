class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s):
        operators, operands = ['#'], []
        priorities = {'#': -1, '+': 0, '-': 0, '*': 1, '/': 1, '(': 2}
        num = 0
        num_flag = False
        
        for i, ch in enumerate(s):
            if ch == ' ':
                continue
            if ch.isdigit():
                num = num * 10 + int(ch)
                num_flag = True
            else:
                if num_flag:
                    operands.append(num)
                num = 0
                num_flag = False
                if ch == ')':
                    while operators[-1] != '(':
                        operator = operators.pop()
                        op2 = operands.pop()
                        op1 = operands.pop()
                        operands.append(self.calc(op1, op2, operator))
                    operators.pop()    # pop out '('
                else:
                    if ch == '(':
                        operators.append(ch)
                    else:
                        while (operators[-1] != '(' and 
                        priorities[operators[-1]] >= priorities[ch]):
                            operator = operators.pop()
                            op2 = operands.pop()
                            op1 = operands.pop()
                            operands.append(self.calc(op1, op2, operator))
                        operators.append(ch)
        
        if num_flag:
            operands.append(num)
            
        while len(operators) > 1:
            operator = operators.pop()
            op2 = operands.pop()
            op1 = operands.pop()
            operands.append(self.calc(op1, op2, operator))
            
        return operands[0]
        
            
    def calc(self, op1, op2, operator):
        if operator == '+': return op1 + op2
        if operator == '-': return op1 - op2
        if operator == '*': return op1 * op2
        if operator == '/': return op1 // op2
            
