class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # output limit exceeded , timeout
        # for i in range(len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         return True
        # return False

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False