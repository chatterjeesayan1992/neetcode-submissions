class Solution:
    def isPalindrome(self, s: str) -> bool:

        l,r = 0, len(s) -1
        s = s.lower()

        while l < r:
            while s[l].isalnum() == False and l < len(s) - 1:
                l += 1
            while s[r].isalnum() == False and r > 0:
                r -= 1
            
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if l < r:
                    return False
        
        return True
        