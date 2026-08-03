class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        for i in range(1,x+1):
            temp=i
            dig_sum=0
            while temp>0:
                dig_sum+=temp%10
                temp //=10
        if x%dig_sum == 0:
            return dig_sum
        else:
            return -1            
        
