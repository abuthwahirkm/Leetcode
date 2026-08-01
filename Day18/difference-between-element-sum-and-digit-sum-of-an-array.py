class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele=0
        dig=0
        for num in nums:
            ele+=num
            while num>0:
                dig+=num%10
                num //=10
        return ele-dig
