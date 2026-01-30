class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max1=0
        for val in sentences:
            x=val.split()
            max1=max(max1,len(x))
        return max1

        