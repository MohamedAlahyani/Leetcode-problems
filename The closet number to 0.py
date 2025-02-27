class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0]  # Start with the first element

        for num in nums:
            # If the absolute value of the current number is smaller, update closest
            if abs(num) < abs(closest):
                closest = num
            # If there's a tie, choose the larger number
            elif abs(num) == abs(closest) and num > closest:
                closest = num

        return closest
