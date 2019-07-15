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
        morse_code = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
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

#Sort Array By Parity
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        parity = []
        odd = []
        for item in A:
            if item % 2 == 0:
                parity.append(item)
            else:
                odd.append(item)
                
        parity.extend(odd)
        
        return parity
                
#N-Repeated Element in Size 2N Array
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        temp = []
        for items in A:
            if items not in temp:
                temp.append(items)
            else:
                return items
                
#Squares of a Sorted Array
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        for i in range(0,len(A)):
            A[i] = A[i]*A[i]
        
        A.sort()
        return A
        
#Robot Return to Origin
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        steps = 0
        
        for step in moves:
            if step == 'U':
                steps+=1
            elif step == 'D':
                steps-=1
            elif step == 'R':
                steps+=10
            else:
                steps-=10
        
        if steps == 0:
            return True
        else:
            return False

#Self Dividing Numbers
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        num = []
        for i in range(left,right+1):
            j = str(i)
            flag=True
            for digit in j:
                if digit == '0' or i % int(digit) != 0:
                    flag = False
                    break
                
            if(flag):
                num.append(i)
        return num
        
#Hamming Distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        v = bin(x ^ y)[2:]
        step = 0
        for i in str(v):
            if i=='1':
                step+=1
        return step

#Unique Email Addresses        
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mails = []
        temp = ''
        domain = ''
        for id in emails:
            temp=(id[:id.find('@')])           
            domain = id[id.find('@'):]
            if temp.find('+') > 0:
                temp = temp[:temp.find('+')]
            temp = temp.replace(".","")
            temp += domain
            mails.append(temp)
        test = []
        for id in mails:
            if id not in test:
                test.append(id)       
        return len(test)

#DI String Match        
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        dec = len(S)
        inc = 0
        pnc = []
        for a in range(0,len(S)):
            if S[a]=="I":
                pnc.append(inc)
                inc+=1
            elif S[a]=="D":
                pnc.append(dec)
                dec-=1
        
        for i in range(0,len(S)+1):
            if i not in pnc:
                pnc.append(i)
                break
                
        return pnc
        
#Peak Index in a Mountain Array
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1,len(A)):
            if A[i]>A[i-1] and A[i]>A[i+1]:
                return i      
                
#Delete Columns to Make Sorted
#Brute Force
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        t = []
        
        for i in range(0,len(A[1])):
            for j in range(0,len(A)):
                t.append(A[j][i])
            for k in range(0,len(t)-1):
                if t[k]>t[k+1]:
                    count+=1
                    break;
            t = []
        return count                     
        
#Optimized
return sum(any(A[j][i] < A[j - 1][i] for j in range(1, len(A))) for i in range(len(A[0])))

#Height Checker
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c = 0
        new_ip = sorted(heights)
        for i in range(len(new_ip)):
            if new_ip[i]!=heights[i]:
                c+=1
        return c
        
#Array Partition I
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sum = 0
        for i in range(0,len(nums),2):
                sum += nums[i]
        return sum
        
#Sort Array By Parity II
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        A = []
        for i in range(0,2*len(odd),2):
            A.append(even[int(i/2)])
            A.append(odd[int(i/2)])
            
        return A

# Occurrences After Bigram
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        res = []
        for i in range(2,len(words)):
            if words[i-2] == first and words[i-1] == second:
                res.append(words[i])
        return res
        
#Fibonacci Number
class Solution:
    def fib(self, N: int) -> int:
        fib = {0:0,1:1}
        for i in range(2,N+1):
                fib[i] = fib[i-1] + fib[i-2]
        
        return fib[N]
        
#Available Captures for Rook      
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        step_i = 0
        step_j = 0
        count = 0
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == 'R':
                    step_i = i
                    step_j = j
                    
        for i in range(step_i,8):
            if board[i][step_j] == 'p':
                count+=1
                break
            elif board[i][step_j] == 'B':
                break
        
        for i in range(step_i,0,-1):
            if board[i][step_j] == 'p':
                count+=1
                break
            elif board[i][step_j] == 'B':
                break
        
        for j in range(step_j,8):
            if board[step_i][j] == 'p':
                count+=1
                break
            elif board[step_i][j] == 'B':
                break
                
        for j in range(step_j,0,-1):
            if board[step_i][j] == 'p':
                count+=1
                break
            elif board[step_i][j] == 'B':
                break

        return count
        
#Find Common Characters        
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cnt = 0
        char = []
        tot = len(A)
        for i in A[0]:
            cnt = 0
            for j in A[1:]:
                if i in j:
                    cnt += 1
            if cnt == tot - 1:
                char.append(i)
                for k in range(0,len(A)):
                    A[k] = A[k].replace(i,'',1)
        return char
        
#Defanging an IP Address
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
        
#Relative Sort Array
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        sec = []
        for i in arr2:
            for j in arr1:
                if j==i:
                    arr.append(j)

        arr1 = sorted(arr1)
        for j in arr1:
            if j not in arr:
                sec.append(j)
        return arr+sec
                    