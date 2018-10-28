class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        expression = ''
        left_brackets = []
        for ch in s:
            if ch == '(':
                left_brackets.append(len(expression))
                expression += ch
            elif ch == ')':
                left_idx = left_brackets.pop()
                sub_result = self.sub_calculate(expression[left_idx + 1:])
                expression = expression[:left_idx]
                if sub_result < 0 and expression and expression[-1] == '-':
                    expression = expression[:-1] + '+' + str(-sub_result)
                else:
                    expression = expression + str(sub_result)
            else:
                expression += ch
                
        return self.sub_calculate(expression)
                    
                    
    def sub_calculate(self, s):
        stack = []
        operator = '+'
        num = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if ch == '+' or ch == '-' or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                if operator == '-':
                    stack.append(-num)
                num = 0
                operator = ch
        return sum(stack)