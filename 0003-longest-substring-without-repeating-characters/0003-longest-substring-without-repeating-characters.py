class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1=0
        temp=set()
        n=len(s)
        l=0
        for i in range(n):
            while s[i] in temp:
                temp.remove(s[l])
                l+=1
            temp.add(s[i])
            max1=max(max1,(i+1)-l)
        return max1

        