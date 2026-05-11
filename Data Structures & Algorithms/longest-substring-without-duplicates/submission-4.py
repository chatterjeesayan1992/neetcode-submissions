class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)
        
        
        from collections import Counter
        l,r = 0,1

        max_len = -sys.maxsize - 1
        while r < len(s)+1:
            substr = s[l:r]
            counts = Counter(substr)
            if max(list(counts.values())) > 1:
                if l < len(s) -1:
                    l += 1
                len_str = 0
            else:
                len_str = len(substr)
                max_len = max(max_len, len_str)
                r += 1
        
        return max_len
        

                
            
        