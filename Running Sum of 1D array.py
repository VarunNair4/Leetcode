class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        index = 1
        while index<len(nums):
            nums[index] = nums[index] + nums[index-1]
            index = index+1
        return nums
