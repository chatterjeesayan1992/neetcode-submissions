class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0

        res = 0
        from collections import Counter

        for r in range(1,len(s) +1):

            substr = s[l:r]
            # print(substr,r,l)
            counts = Counter(substr)

            if max(counts.values()) > 1:
                l += 1
            else:
                res = max(res, r - l)
        
        return res




                
            
        