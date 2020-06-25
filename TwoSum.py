class Solution:
    def twoSum(self, list_nums: List[int], target: int) -> List[int]:
        d = {}
        
           
        for i in range(len(list_nums)):    
            if target - list_nums[i] in d:
                print(d)
                return [d[target-list_nums[i]],i]
            
            d[list_nums[i]] = i
            
        return -1
    
