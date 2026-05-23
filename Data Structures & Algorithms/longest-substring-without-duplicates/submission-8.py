class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        from collections import Counter

        res = 0
        for r in range(1, len(s)+1):
            substr = s[l:r]

            count_substr = Counter(substr)

            if max(count_substr.values()) > 1:
                l += 1
            
            else:
                res = max(res, r - l)

        return res            





                
            
        