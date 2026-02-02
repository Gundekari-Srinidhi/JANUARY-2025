class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for val in words:
            if val==val[::-1]:
                return val
        return ""
                
        