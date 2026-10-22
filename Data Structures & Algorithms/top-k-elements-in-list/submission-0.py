class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        count=0
        for i in nums:
            if(i not in freq):
                freq[i]=1
            else:
                freq[i]+=1
        sorted_freq=sorted(freq.items(),key=lambda item:item[1],reverse=True)
        op=[]
        for key,value in sorted_freq:
            op.append(key)
            count+=1
            if(count >= k):
                return op
        return op


        