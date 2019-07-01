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
		
#Remove Outermost Parentheses
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        t = ''
        stack = []
        items = []
        for s in S:
            strin = ''
            if s == '(':
                stack.append(s)
                t = t+s
            elif s == ')':
                t = t+s
                stack.pop()
            
            if len(stack) == 0:
                items.append(t)
                t = ''
                
        for i in items:
            t = t + i[1:-1]
           
        return t
            
            
