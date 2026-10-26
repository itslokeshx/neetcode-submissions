class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr=[0]*len(nums)
        suffix_arr=[0]*len(nums)
        prefix=1
        suffix=1

        op=[0]*len(nums)

        for i in range(0,len(nums)):
            prefix_arr[i] = prefix
            prefix*=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            suffix_arr[i] = suffix
            suffix*=nums[i]

        for i in range(len(nums)):
            op[i]=prefix_arr[i] * suffix_arr[i]
        
        return op
        


        


        