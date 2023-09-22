class Solution(object):
    def twoSum(self, nums, target):
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j :
                    output.append(i)
                    output.append(j)

                    return output