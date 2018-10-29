class MinStack:
    
    def __init__(self):
        self.stack = []
    
    def push(self, number):
        if self.stack and self.stack[-1][1] < number: 
            self.stack.append([number, self.stack[-1][1]])
        else: self.stack.append([number, number])
    
    def pop(self):
        return self.stack.pop()[0]
    
    def min(self):
        return self.stack[-1][1]

# class MinStack:
    
#     def __init__(self):
#         self.stack = []
#         self.mini = []

#     """
#     @param: number: An integer
#     @return: nothing
#     """
#     def push(self, number):
#         self.stack.append(number)
#         i = 0
#         while i < len(self.mini) and number > self.mini[i]: i += 1
#         self.mini.insert(i, number)
            
#     """
#     @return: An integer
#     """
#     def pop(self):
#         number = self.stack.pop()
#         self.mini.remove(number)
#         return number

#     """
#     @return: An integer
#     """
#     def min(self):
#         return self.mini[0]