#Jewels and Stones

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        items = 0
        for stones in S:    
            for jewels in J:
                if stones == jewels:
                    items+=1
                    break
        
        return items      
		
