class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        stack = []
        operator = '+'
        num = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if ch != " " and not ch.isdigit() or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                else:  # '/'
                    stack.append(int(stack.pop() / num))
                num = 0
                operator = ch
                
        return sum(stack)