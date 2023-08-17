class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1
        k = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                c = c + 1
            else:
                c = 1

            if c <= 2:
                nums[k] = nums[i]
                k = k + 1

        return k