class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        nums.sort()
        seen=set()
        seen.add(nums[0])
        count=1
        op=0

        for i in range(1,len(nums)):
            if((nums[i] == nums[i-1] + 1) and nums[i] not in seen):
                count+=1
            elif( nums[i] == nums[i-1] ):
                continue
            else:
                op=max(op,count)
                count=1
        op=max(op,count)
        return op

            
        