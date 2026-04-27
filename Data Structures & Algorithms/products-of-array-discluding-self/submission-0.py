class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prefix_arr = []
        postfix_arr = []
        res = []

        prefix_prod = 1
        postfix_prod = 1

        for n in nums:
            prefix_prod *= n
            prefix_arr.append(prefix_prod)
        
        for i in range(len(nums) -1, -1, -1):
            postfix_prod *= nums[i] 
            postfix_arr = [postfix_prod] + postfix_arr
        
        
        for i,n in enumerate(nums):

            if i >= 1:
                prefix_prod = prefix_arr[i-1]
            else:
                prefix_prod = 1
            
            if i < len(nums) - 1:
                postfix_prod = postfix_arr[i+1]
            else:
                postfix_prod = 1
            
            res.append(prefix_prod * postfix_prod)
            

  
        return res
        