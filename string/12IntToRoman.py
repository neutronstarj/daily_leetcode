class Solution:
    def intToRoman(self, num: int) -> str:
        symList=[["I",1],["IV",4],["V",5],["IX",9],["X",10]
        ,["XL",40],    ["L",50],["XC",90],["C",100],
        ["CD",400],["D",500],["CM",900],["M",1000]]
        #dont use map because we need this order
        res=""
        for sym, val in reversed(symList):
            #if the current number divide the current symlist val
            #can output an int 
            if num // val:
               count = num//val
               res+=(sym*count)
               num = num-(count*val)
        return res



        
