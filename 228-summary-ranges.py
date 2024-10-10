class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        arr = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            if start == nums[i]:
                arr.append(str(start))
            else:
                arr.append(f"{start}->{nums[i]}")
            
            i += 1

        return arr