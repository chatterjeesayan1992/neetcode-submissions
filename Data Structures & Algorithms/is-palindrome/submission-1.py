class Solution:
    def isPalindrome(self, s: str) -> bool:

        low,high = 0,len(s)-1
        s = s.lower()

        while low < high:
            while s[low].isalnum() == False and low < len(s)-1:
                low += 1
            while s[high].isalnum() == False and high > 0:
                high -= 1
            
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                if low < high:
                    return False
                            
        return True
        