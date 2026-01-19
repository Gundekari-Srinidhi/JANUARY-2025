class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=0
        r=k-1
        Sum=sum(cardPoints[:k])
        j=len(cardPoints)-1
        max_Sum=Sum
        while j>=(len(cardPoints)-k):
            Sum-=cardPoints[r]
            Sum+=cardPoints[j]
            r-=1
            j-=1
            max_Sum=max(max_Sum,Sum)
        return max_Sum
        