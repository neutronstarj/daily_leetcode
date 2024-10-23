class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    ##idea count the appearance, if this apparence  is 0, mark to 1, make it to new place 
    ##init an empty array 
        sortedArray=[]
        ##should be a dictionary that key is nums[i], value is the occrance 
        for i in range(len(nums)):
            if nums[i] not in sortedArray:
                sortedArray.append(nums[i])
        #it is for checking that inplace
        for i in range(len(sortedArray)):
            nums[i] = sortedArray[i]
        

        return len(sortedArray)
