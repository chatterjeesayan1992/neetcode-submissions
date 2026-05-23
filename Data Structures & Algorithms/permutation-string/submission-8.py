class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        count_s1 = Counter(s1)
        l = 0
        for r in range(len(s1), len(s2)+1):
            substr = s2[l:r]
            count_substr = Counter(substr)

            if count_s1 == count_substr:
                return True
            else:
                l += 1
        
        return False
        


            




     
        