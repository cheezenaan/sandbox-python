class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if not nums:
            return False

        nums = sorted(nums)
        prev = nums[0]

        for n in nums[1:]:
            if n == prev:
                return True
            else:
                prev = n

        return False
