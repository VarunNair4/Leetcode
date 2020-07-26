class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(0,len(nums)//2):
            a += [nums[2*i+1]] * nums[2*i]
        return a
            
