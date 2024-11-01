class RandomizedSet:

    def __init__(self):
        self.numMap = {} #hashmap
        self.numList = []

        

    def insert(self, val: int) -> bool:
        result = val  not in self.numMap
        #if not in the map, add to both ap and list 
        if result:
            self.numMap[val]=len(self.numList) 
            #insert the value, store the index of the values in numlist 
            self.numList.append(val)
        return result 
        

    def remove(self, val: int) -> bool:
        result = val in self.numMap
        if result:
            idx = self.numMap[val] #get the index
            LastVal = self.numList[-1]

            self.numList[idx]=LastVal
            self.numList.pop()
            self.numMap[LastVal]=idx #update the index 
            del self.numMap[val]
        return result #return true is in the num map 

        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
