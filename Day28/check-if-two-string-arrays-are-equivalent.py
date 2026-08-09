class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a1=""
        b1=""

        for word in word1:
            a1+=word
        for word in word2:
            b1+=word
        return a1==b1        

        
