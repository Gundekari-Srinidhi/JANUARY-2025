class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        char_count={'a':0,'b':0,'c':0}
        left=0
        for right in range(n):
            char_count[s[right]]+=1
            while char_count['a']>0 and char_count['b']>0 and char_count['c']>0:
                count+=n-right
                char_count[s[left]]-=1
                left+=1
        return count
