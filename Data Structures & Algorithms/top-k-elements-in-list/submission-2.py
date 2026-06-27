class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        count_nums = Counter(nums)

        count_nums_sorted = dict(sorted(count_nums.items(), key = lambda x: x[1], reverse = True))

        return list(count_nums_sorted.keys())[:k]

