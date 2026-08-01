class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul=1
        adi=0
        while n>0:
            digit=n%10
            mul=mul*digit
            adi=adi+digit
            n//=10
        return mul-adi    

        
