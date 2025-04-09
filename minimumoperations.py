class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        len = 0
        for i in nums:
            if i < k:
                return -1
            elif i == k:
                continue
            elif i in seen:
                continue
            else:
                len += 1
            seen.add(i)
        return len
