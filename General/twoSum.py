""" Description:
Get a list of integers: nums
get a target value: target

Return a single pair of indeces that sum to that target
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i


