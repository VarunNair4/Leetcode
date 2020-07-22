class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        XOR = 0
        nums = []
        for i in range (0,n):
            nums.append(start + 2 *i)
        for i in nums:
            XOR = XOR ^ i
        return XOR
