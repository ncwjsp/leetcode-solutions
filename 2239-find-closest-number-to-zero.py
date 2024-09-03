from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        arr = [float("inf")]
        for i in nums:
            if i == 0:
                return i
            elif i > 0 and i < abs(arr[0]):
                arr[0] = i
            elif i < 0 and abs(i) < abs(arr[0]):
                arr[0] = i
            elif abs(i) == abs(arr[0]):
                arr.append(i)
        return max(arr)
