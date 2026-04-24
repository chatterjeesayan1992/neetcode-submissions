class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        idx_dict = {num : i for (i,num) in enumerate(nums)}

        for i,num in enumerate(nums):
            other_idx = idx_dict.get(target - num, -1)

            if other_idx != -1 and i != other_idx:
                return [i, other_idx]
        

            


        