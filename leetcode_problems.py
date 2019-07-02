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
            
#To Lower Case
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()  

#Unique Morse Code Words
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = {'a':".-",
                      'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        t = ''
        items = []
        for word in words:
            for s in word:
                t =  t + morse_code[s]
            items.append(t)
            t = ''
        
        unique_list = []
        for item in items:
            if item not in unique_list:
                unique_list.append(item)
        return len(unique_list)

#Flipping an Image
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for lst in A:
            lst.reverse()
          
        tup = []
        lst = []
        for item in A:
            for itm in item:
                if itm == 0:
                    lst.append(1)
                else:
                    lst.append(0)
            tup.append(lst)
            lst = []
        
        return tup                