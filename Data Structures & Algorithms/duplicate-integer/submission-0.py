class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        count_dict = Counter(nums)

        for key in count_dict:
            if count_dict[key] > 1:
                return True

        return False
        