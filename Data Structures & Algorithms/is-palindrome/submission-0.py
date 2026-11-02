class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        s=s.lower()
        for i in s:
            if(re.match(r"^[a-zA-Z0-9]+$",i)):
                s1+=i
        s2=s1[::-1]
        if(s1==s2):
            return True
        else:
            return False
        