class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_idcs = {num:i for (i,num) in enumerate(nums)}


        for i in range(len(nums)):
            other_num = target - nums[i]

            other_index = num_idcs.get(other_num,None) 

            if other_index != None and i!=other_index:
                return [i,other_index]
        


        



            


        