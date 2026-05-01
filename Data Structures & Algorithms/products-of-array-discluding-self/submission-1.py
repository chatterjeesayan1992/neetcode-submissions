class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_arr = []
        postfix_arr = []
        prefix_prod = 1
        postfix_prod = 1
        for n in nums:
            prefix_prod *= n
            prefix_arr.append(prefix_prod)
        
        for i in range(len(nums)-1, -1, -1):
            postfix_prod *= nums[i]
            postfix_arr = [postfix_prod] + postfix_arr
        
        res = []

        for i in range(len(nums)):

            if i > 0:
                prefix = prefix_arr[i-1]
            else:
                prefix = 1
            
            if i < len(nums)-1:
                postfix =  postfix_arr[i+1]
            else:
                postfix = 1
            
            res.append(prefix * postfix)
        
        return res
            
        
