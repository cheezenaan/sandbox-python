class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums = sorted(nums)
        prev = None

        for n in nums:
            if n == prev:
                return True
            else:
                prev = n

        return False
