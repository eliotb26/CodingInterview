"""
This is the course over winter break to practice for techincal coding interviews by NYU Tandon PHD student Shantanu Tripathi

Also taking notes in the physical notebook and it is recorded. This
Date: 1/11/2021

"""


#1. https://leetcode.com/problems/minimum-size-subarray-sum/

#n positive integers 
# s
#sum >= s
#return 0 if not 
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_len =  len(nums) + 1   #larger than the len 
        beg, end = 0, 0 
        summ = 0 
        for end in range(len(nums)): 
            summ += nums[end]
            while(summ >=s): 
                #shrinking
                min_len = min(min_len, end-beg+1)
                summ -= nums[beg]
                beg += 1
        if min_len == len(nums) + 1: 
            return 0 
        return min_len

#2. https://leetcode.com/problems/k-diff-pairs-in-an-array/
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort() 
        beg, end = 0, 0 
        counter = 0 
        sz = len(nums)
        for beg in range(len(nums)-1):      #begining can never reach last index
            if (beg>0 and nums[beg] == nums[beg - 1]): 
                continue        #so unique diff pairs 
            end = max(beg + 1, end)
            while (end<sz and nums[end] - nums[beg] < k):
                end += 1 
            if end==sz: 
                break
            if nums[end] - nums[beg] == k: 
                counter += 1 
        return counter


#3. https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """        
        sz = len(height)
        left_max = 0 
        right_max = 0 
        b = 0 
        e = sz -1
        ans = 0
        while (b<e): 
            left_max = max(left_max, height[b])
            right_max = max(right_max, height[e])
            if left_max <= right_max: 
                ans += left_max - height[b]
                b += 1 
            else: 
                ans += right_max - height[e]
                e -= 1 
        return ans





###DIVIDE AND CONQUER TECHNIQUE 

#53. https://leetcode.com/problems/maximum-subarray/


#sliding window approach 
#save max_sum and compare with the prefix if its positive and beneficial or not
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0 
        max_sum = nums[0]
        
        for elem in nums: 
            if curr_sum < 0:        #where prefix is negative, disclude it and start over
                curr_sum = 0
            curr_sum += elem         #add elem to the current sum 
            max_sum = max(curr_sum, max_sum)     #even if add to the current sum, a previous 
                                                #subarray could be greater
        return max_sum
        




### Lecture 3 

##



# 239. https://leetcode.com/problems/sliding-window-maximum/




# 739  https://leetcode.com/problems/daily-temperatures/

# [73, 74, 75, 71, 69, 72, 76, 73]

# max_structure = [73, ] 
#

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        sz = len(T)
        stack = [] 
        ans = [0]*sz
        for ind in range(len(T)): 
            while(stack and T[stack[-1]] < T[ind]): 
                ans[stack[-1]] = ind - stack[-1]
                stack.pop()
            stack.append(ind)
        return ans

