class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        minlen = float('inf')
        sind = 0
        d = {}
        count = 0
        n = len(s)

        for ch in t:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        while r < n:
            if s[r] in d:
                if d[s[r]] > 0:
                    count += 1
                d[s[r]] -= 1

            while count == len(t):
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    sind = l

                if s[l] in d:
                    d[s[l]] += 1
                    if d[s[l]] > 0:
                        count -= 1
                l += 1

            r += 1

        if minlen == float('inf'):
            return ""
        return s[sind:sind + minlen]
