class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        fir=1
        sec=2

        for i in range(3,n+1):
            curr=fir+sec
            fir=sec
            sec=curr
        return sec        
