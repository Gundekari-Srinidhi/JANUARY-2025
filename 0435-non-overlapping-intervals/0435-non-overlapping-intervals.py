class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key = lambda x:x[1])
        count=1
        freetime=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]>=freetime:
                count+=1
                freetime=intervals[i][1]
        return (n-count)

        