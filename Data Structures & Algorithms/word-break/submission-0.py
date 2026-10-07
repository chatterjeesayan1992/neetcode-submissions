class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False]*(len(s) + 1)

        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            for w in wordDict:
                if (i+len(w)) <= len(s):
                    if w == s[i: i+len(w)]:
                        # print(s[i: i+len(w)])
                        # print('yes')
                        dp[i] = dp[i + len(w)]
                    if dp[i]:
                        break
        
        print(dp)
        
        return dp[0]
        