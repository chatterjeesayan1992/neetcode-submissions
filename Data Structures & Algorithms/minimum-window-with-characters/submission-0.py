class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""
        window, countT = {},{}

        for c in t:
            countT[c] = countT.get(c,0) + 1
        
        have,need = 0, len(countT)
        print(have, need)
        min_sol, minsol_len = [-1,-1], float("infinity")

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                print('yes')
                if (r - l + 1) < minsol_len:
                    minsol_len = (r - l + 1)
                    min_sol = [l,r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1                
                l += 1
        l,r = min_sol

        return s[l: r + 1] if minsol_len != float("infinity") else "" 
   



        

