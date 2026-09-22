class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(set(nums))

        if not nums:
            return 0

        count = 1
        best = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
                best = max(best, count)
            else:
                count = 1

        return best