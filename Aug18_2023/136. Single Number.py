class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # l = list(set(nums))
        # for i in l:
        #     if nums.count(i)==1:
        #         return(i)

        nums.sort()
        print(nums)
        for i in range(0, len(nums) - 1, 2):
            if nums[i] == nums[i + 1]:
                continue
            else:
                return nums[i]

        return nums[len(nums) - 1]
