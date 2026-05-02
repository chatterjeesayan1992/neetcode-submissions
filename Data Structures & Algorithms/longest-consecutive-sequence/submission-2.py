class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        counter_nums = collections.Counter(nums)

        counter_nums_sorted = sorted(counter_nums.items(), key=lambda k: k[0])


        maxlen = 1
        prev = counter_nums_sorted[0][0]
        res = []
        length = 1
        for i,(key,val) in enumerate(counter_nums_sorted):

            if i == 0:
                continue
            else:
                if key - prev == 1:
                    length += 1
                    maxlen = max(length, maxlen)
                else:
                    length = 1
            
            prev = key
        
        return maxlen




            

