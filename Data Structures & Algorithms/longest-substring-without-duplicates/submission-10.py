class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        from collections import Counter
        max_len = 0

        max_substr = ''

        for r in range(len(s)):
            substr = s[l: r+1]
            count_substr = Counter(substr)

            if max(count_substr.values()) > 1:
                l += 1

            max_len = max(max_len, r - l + 1)
            # max_substr = substr
        
        return max_len








                
            
        