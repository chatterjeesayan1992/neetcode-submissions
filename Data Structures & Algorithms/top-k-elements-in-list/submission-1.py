class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        count_dict = Counter(nums)

        count_dict_sorted = dict(sorted(count_dict.items(), key=lambda k: k[1], reverse=True))

        return list(count_dict_sorted.keys())[:k]