class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n

        count = 1
        max_count = 1
        has_diff = False

        for i in range(1, n):
            if arr[i] != arr[i-1]:
                has_diff = True

        for i in range(1, n - 1):
            if (arr[i-1] > arr[i] < arr[i+1]) or (arr[i-1] < arr[i] > arr[i+1]):
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

        if max_count > 1:
            return max_count + 1
        return 2 if has_diff else 1
