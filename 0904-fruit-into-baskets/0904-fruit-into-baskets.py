class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left,right=0,0
        n=len(fruits)
        d={}
        max_len=0
        while right<n:
            if fruits[right] in d:
                d[fruits[right]]+=1
            else:
                d[fruits[right]]=1
            while len(d)>2:
                d[fruits[left]]-=1
                if d[fruits[left]]==0:
                    del d[fruits[left]]
                left+=1
            max_len=max(max_len,right+1-left)
            right+=1
        return max_len

        