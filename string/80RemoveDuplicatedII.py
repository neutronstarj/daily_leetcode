class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        occuranceDict = {}
        j= 0
        for i in range(len(nums)):
            num = nums[i]
            if num not in occuranceDict:
                occuranceDict[num]=1
                nums[j]=num #so inplace
                j+=1
            elif occuranceDict[num]<2:
                occuranceDict[num]+=1
                nums[j]=num
                j+=1
                ##we don't care if the occurance =2 and greater than 2
        return j
