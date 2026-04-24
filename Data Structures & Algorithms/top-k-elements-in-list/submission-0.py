class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        counts = Counter(nums)
        
        counts_sorted = dict(sorted(counts.items(), key= lambda k:k[1], reverse=True))
        return list(counts_sorted.keys())[:k]