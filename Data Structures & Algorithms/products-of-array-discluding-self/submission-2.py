class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l=[0]*n
        r=[0]*n
        s=[0]*n

        l[0]=r[n-1]=1
        for i in range(1,n):
            l[i] = nums[i-1]*l[i-1]
        
        for j in range(n-2,-1,-1):
            r[j] = nums[j+1]*r[j+1]
        
        for i in range(0,n):
            s[i] = l[i]*r[i]
        
        return s
            
            


