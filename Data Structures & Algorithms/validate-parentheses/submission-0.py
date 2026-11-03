class Solution:
    def push(self,l, b):
        l.append(b)

    def top(self,l):
        if(len(l)==0):
            return -1
        return l[-1]

    def opening(self,ch):
        if(ch=='{'or ch=='[' or ch=='('):
            return True
        else:
            return False

    def closing(self,ch):
        if(ch=='}' or ch==']'or ch==')'):
            return True
        else:
            return False
    
    def check(self,o,c):
        if(o=='{' and c=='}'):
            return True
        elif(o=='(' and c==')'):
            return True
        elif(o=='[' and c==']'):
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        l=[]
        for i in range(0,len(s)):
            ch = s[i]
            if(self.opening(ch)):
                self.push(l,ch)
            
            elif (self.closing(ch)):
                o=self.top(l)
                if(self.check(o,ch)==False):
                    return False
                else:
                    l.pop(-1)
        
        if(len(l)==0):
            return True
        else:
            return False



        