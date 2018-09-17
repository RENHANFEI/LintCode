# class Solution:
#     """
#     @param num1: a non-negative integers
#     @param num2: a non-negative integers
#     @return: return sum of num1 and num2
#     """
#     def addStrings(self, num1, num2):
#         minDigit = min(len(num1), len(num2))
#         longerNum = num1 if len(num1) > len(num2) else num2

#         carry = 0
#         result = ""

#         for i in range(minDigit):
#             cur = int(num1[-i-1]) + int(num2[-i-1]) + carry
#             result = str(cur % 10) + result
#             carry = cur // 10

#         for i in range(len(longerNum) - minDigit):
#             if carry != 0:
#                 cur = int(longerNum[-i-minDigit-1]) + carry
#                 result = str(cur % 10) + result
#                 carry = cur // 10
#             else:
#                 result = longerNum[:-i-minDigit] + result
#                 break

#         if carry != 0:
#             result = str(carry) + result

#         return result
            

# class Solution:
#     """
#     @param num1: a non-negative integers
#     @param num2: a non-negative integers
#     @return: return sum of num1 and num2
#     """
#     def addStrings(self, num1, num2):
#         maxDigit = max(len(num1), len(num2))
#         minDigit = min(len(num1), len(num2))
#         longerNum = (num1 if len(num1) > len(num2) else num2)[:-minDigit]
#         carry = 0
#         result = ""

#         for i in range(minDigit):
#             cur = int(num1[-i-1]) + int(num2[-i-1]) + carry
#             result = str(cur % 10) + result
#             carry = cur // 10

#         for i in range(maxDigit - minDigit):
#             if carry == 0:
#                 break
#             else:
#                 cur = int(longerNum[-i-1]) + carry
#                 longerNum = longerNum[:-i-1] + str(cur % 10) if i == 0 \
#                         else longerNum[:-i-1] + str(cur % 10) + longerNum[-i:]
#                 carry = cur // 10
        
#         result = longerNum + result
        
#         if carry != 0:
#             result = str(carry) + result

#         return result    

class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        cursor1 = len(num1) - 1
        cursor2 = len(num2) - 1

        result = ""
        carry = 0

        while cursor1 >= 0 or cursor2 >= 0:

            if cursor1 >= 0:
                digit1 = int(num1[cursor1])
            else:
                digit1 = 0
            if cursor2 >= 0:
                digit2 = int(num2[cursor2])
            else:
                digit2 = 0

            cur = digit1 + digit2 + carry
            result = str(cur % 10) + result
            carry = cur // 10

            cursor1 -= 1
            cursor2 -= 1

        if carry > 0:
            result = str(carry) + result

        return result

sol = Solution()
x = "4"
y = "1"

print(sol.addStrings(x,y))


# class Solution:
#     """
#     @param num1: a non-negative integers
#     @param num2: a non-negative integers
#     @return: return sum of num1 and num2
#     """
#     def addStrings(self, num1, num2):
#         digitNum = max(len(num1), len(num2))
#         num1 = "0" * (digitNum - len(num1)) + num1
#         num2 = "0" * (digitNum - len(num2)) + num2

#         carry = 0
#         result = ""

#         for i in range(digitNum):
#             cur = int(num1[-i-1]) + int(num2[-i-1]) + carry
#             result = str(cur % 10) + result
#             carry = cur // 10

#         if carry != 0:
#             result = str(carry) + result

#         return result
