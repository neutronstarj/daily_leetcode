class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Create a dictionary to store occurrences
        Occurrence = {}
        
        # Iterate over the list
        for i in range(len(nums)):
            if nums[i] not in Occurrence:
                # Add the element with an initial count of 1
                Occurrence[nums[i]] = 1
            else:
                # Increment the count for the element
                Occurrence[nums[i]] += 1
        
        # Find the key with the maximum value in the dictionary
        max_key = max(Occurrence, key=Occurrence.get)
        
        return max_key
