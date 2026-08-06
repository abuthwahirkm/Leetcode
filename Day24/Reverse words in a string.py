class Solution:
    def reverseWords(self, s: str) -> str:
        word=""
        ans=""
        for ch in s:
            if ch==" ":
                ans+=word[::-1]
                ans+=" "
                word=""
            else:
                 word+=ch
        ans+=word[::-1]     
        return ans              

        
