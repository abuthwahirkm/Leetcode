class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=0
        r=0
        blank=0


        for ch in moves:
            if ch == 'L':
                l+=1
            elif ch== 'R':
                r+=1
            else:
                 blank +=1
        return abs(l-r)+blank
                 
