"""
Desc: Given an int array nums, return true if any value appears at least twice in the array, and return false if every element is distince
"""

def containsDuplicate(self, nums: List[int]) -> bool:
        myMap = {} 
        for ind, value in enumerate(nums):
            print(value in myMap)
            if value in myMap:
                return True
            myMap[value] = ind
        return False

O(n) time, O(1) space
