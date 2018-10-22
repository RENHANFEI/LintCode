class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        
        result = []
        
        for i, n in enumerate(numbers):
            for j, m in enumerate(numbers[i+1:]):
                s = m + n
                if -s in numbers[j+i+2:]:
                    if sorted([n, m, -s]) not in result:
                        result.append(sorted([n, m, -s]))
                    
        return result