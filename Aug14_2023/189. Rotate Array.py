class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Solution 1: accepted successfully
        for i in range(k):
            nums.insert(0,nums.pop(len(nums)-1))

        #Solution 2: time limit exceeded
        # for k in range(k):
        #     for i in range(len(nums)):
        #         temp = nums[len(nums)-1]
        #         nums[len(nums)-1]= nums[i]
        #         nums[i] = temp


