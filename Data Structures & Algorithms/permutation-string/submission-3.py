class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        l,r = 0, len(s1)
        count_s1 = Counter(s1).items()

        while r < len(s2) +1 :
            substr = s2[l:r]
            count_substr = Counter(substr).items()         

            if count_s1 == count_substr:
                return True
            else:
                r += 1
                l += 1
        
        return False


     
        