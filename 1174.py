class Solution:
    """
    @param n: an integer
    @return: the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n
    """
    def nextGreaterElement(self, n):
        
        str_n = str(n)
        if len(str_n) <= 1:
            return -1
        
        list_n = [int(nn) for nn in str_n]
        for i in range(len(list_n) - 1):
            now_consider = i + 2
            temp = list_n[-now_consider:]
            if temp[0] == max(temp):
                continue
            else:
                now_first = temp[0]
                temp.sort()
                for t in temp:
                    if t > now_first:
                        temp.remove(t)
                        temp_result = [t] + temp
                        break
                result_list = list_n[:-i-2] + temp_result
                result = 0
                for r in result_list:
                    result = result * 10 + r
                if result > 2 ** 31 - 1:
                    return -1
                return result
            
        return -1
                
            