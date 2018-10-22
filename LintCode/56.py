class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        num_dict = dict()
        for i, number in enumerate(numbers):
            if number in num_dict:
                return num_dict[number], i
            num_dict[target - number] = i