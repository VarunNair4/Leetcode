class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=0
        nums = Counter(nums).values()
        for i in nums:
            if i > 1:
                a = a + i*(i-1)//2
        return a
