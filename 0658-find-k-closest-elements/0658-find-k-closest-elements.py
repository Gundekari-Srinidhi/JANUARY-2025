class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=[]
        n=len(arr)
        j=k
        for i in range(n):
            if len(l)<k:
                l.append(arr[i])
            else:
                if abs(arr[i]-x)<abs(l[0]-x):
                    l.pop(0)
                    l.append(arr[i])
        l.sort()
        return l
            
        