from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False

        c1=Counter(s)
        c2=Counter(t)
        
        if(len(c1)!=len(c2)):
            return False
        
        for i in c1:
            if i not in c2:
                return False
            
            v1=c1.get(i)
            v2=c2.get(i)
            
            if(v1!=v2):
                return False
        return True
        
        