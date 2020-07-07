class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array = []
        for i in range(n):
            array.append(nums[i])
            array.append(nums[i+n])        
        return array
