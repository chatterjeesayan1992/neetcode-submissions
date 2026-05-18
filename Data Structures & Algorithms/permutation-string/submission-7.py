class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        from collections import Counter
        
        count_s1 = Counter(s1)
        for r in range(len(s1),len(s2)+1):
            substr = s2[l:r]
            print(substr)

            if Counter(substr) == count_s1:
                return True
            
            else:
                l += 1
        
        return False





     
        