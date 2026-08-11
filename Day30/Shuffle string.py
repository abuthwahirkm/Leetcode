class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_new = [""] * len(indices)
        for i in range(len(indices)):
            s_new[indices[i]]=s[i]
        return "".join(s_new)
