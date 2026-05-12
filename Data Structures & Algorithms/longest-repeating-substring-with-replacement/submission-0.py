class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0

        count_dict ={}

        res = 0
        for r in range(len(s)):
            count_dict[s[r]] = count_dict.get(s[r],0) + 1
            
            while (r - l + 1) - max(count_dict.values()) > k:
                count_dict[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        
        return res




        