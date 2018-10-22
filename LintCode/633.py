class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        head = 0
        slow = nums[head]
        fast = nums[nums[head]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = head
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            
        return slow
