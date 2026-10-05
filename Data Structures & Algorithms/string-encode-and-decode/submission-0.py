class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s=s+str(len(i))+'#'+i+'#'
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        l=[]
        k=0
        while k<=(len(s)-1):
            j=k
            n=""
            while(s[j]!='#'):
                n+=s[j]
                j+=1
            
            n=int(n)
            l.append(s[j+1:j+n+1])
            k=j+n+2
        return l


        

