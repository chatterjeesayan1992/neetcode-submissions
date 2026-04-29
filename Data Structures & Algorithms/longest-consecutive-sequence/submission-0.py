class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) ==0:
            return 0

        count_nums = Counter(nums)

        count_nums = sorted(count_nums.items(), key=lambda k:k[0])

        prev=count_nums[0][0]

        res = []
        maxlen = 1
        length =1
        for i,(key,val) in enumerate(count_nums):    
            if i == 0:
                continue
            else:
                if key - prev == 1:
                    length += 1
                    maxlen = max(maxlen,length)
                else:
                    length = 1
            prev = key
            
        return maxlen
            

