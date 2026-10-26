class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr=[0]*len(nums)
        suffix_arr=[0]*len(nums)
        prefix=1
        suffix=1

        op=[0]*len(nums)

        for i in range(0,len(nums)):
            op[i] = prefix
            prefix*=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            op[i] *= suffix
            suffix*=nums[i]

        return op
        


        


        