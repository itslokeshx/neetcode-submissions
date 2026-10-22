class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[]
        op=[]
        for i in nums:
            if(i not in freq):
                freq[i]=1
            else:
                freq[i]+=1

        heap=[]

        for key,value in freq.items():
            heapq.heappush(heap,(-value,key))
        
        for i in range(k):
            ans.append(heapq.heappop(heap))
        
        for value,key in ans:
            op.append(key)

        return op


        