class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        count = 0
        pointer1_index = 0

        pointer2_index = 0

        for i in range(len(nums) - 1):
            if i + nums[i] > pointer1_index:
                # print("pointer 1: before", i, pointer1_index)
                # print("pointer 2: before", i, pointer2_index)
                pointer1_index = i + nums[i]

            if i == pointer2_index:
                # print(i)
                count = count + 1
                pointer2_index = pointer1_index
        # print("pointer 1:", i,pointer1_index)
        # print("pointer 2:", i, pointer2_index)

        return (count)









