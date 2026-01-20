class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        d={}
        n=len(s)
        maxlen=0
        while r<n:
            if s[r] in d:
                d[s[r]]+=1
            else:
                d[s[r]]=1
            maxFreq=max(d.values())
            while (r-l+1-maxFreq)>k:
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
