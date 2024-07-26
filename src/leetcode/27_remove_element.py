class Solution:
    def remove_elements(self, nums: list[int], val: int) -> int:
        nums[:] = list(filter(lambda n: n != val, nums))
        return len(nums)
