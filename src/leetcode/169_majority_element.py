class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        ans = nums[0]

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

            if counts[num] > counts[ans]:
                ans = num

        return ans
