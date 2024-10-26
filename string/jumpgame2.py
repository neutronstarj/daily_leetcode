class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        #sliding window index
        while r < len(nums)-1:
            #this is at each step find the max 
            farthest = 0
            for i in range( l,r+1):
                #make right value includsive
                farthest = max(farthest, i+nums[i])
                #i + nums[i] is the location
            l=r+1
            r=farthest
            res+=1 #one step 
        return res

        
