class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans=""
        for ch in s:
            ans+=ch
            if ch==" ":
                k-=1
                if k==0:
                    return ans[:-1]

        return ans            
