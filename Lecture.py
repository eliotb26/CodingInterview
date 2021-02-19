"""
This is the course over winter break to practice for techincal coding interviews by NYU Tandon PHD student Shantanu Tripathi

Also taking notes in the physical notebook and it is recorded. This
Date: 1/11/2021

All code is on his git https://github.com/shantanutrip/Blog_codes

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

    #Problem: Not fast enough ; Simple solution
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sz = len(nums)
        ret = []
        
        for ind in range(sz-k+1):
            curr_max = max(nums[ind:ind+k])
            ret.append(curr_max)
            
        return ret 


    #inclass solution 
from collections import deque
def maxSlidingWindow(nums, k):
    sz = len(nums)
    dq = deque() 
    print(dq)
    ans = [] 
    print(dq)
    # for ind in range(len(nums)): 
    #     while (dq and ind - dq[-1] >= k):   
    #         dq.pop()
    #     while (dq and nums[dq.back()] M= nums[ind]): 
    #         dq.pop_back()
    #     dq.back(ind)
    #     if (ind >= k-1): 
    #         ans.push_back(nums[dq.front()])
    
    # return ans

def main(): 
    nums = [1,4,2,6,9]
    k = 3
    maxSlidingWindow(nums, k)
main()


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




### Lecture 1/25/21 
#Binary Trees



# 105 https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.inorder_location = {} 
        self.preorder = [] 
        self.inorder = [] 
        self.preorder_pointer = 0 
        
    def treeBuilder(self, left, right): 
        #take left and right indecies and build the tree
        if left > right: 
            #not possible
            return None
        if left == right: 
            #one element in list
            newNode = TreeNode(val = self.preorder[self.preorder_pointer])
            self.preorder_pointer += 1 
            return newNode
        
        preorder_element = self.preorder[self.preorder_pointer]
        element_inorder_location = self.inorder_location[preorder_element]
        self.preorder_pointer += 1 
        
        #recurssive call on left and right halves
        leftSubtree = self.treeBuilder(left,element_inorder_location-1)
        rightSubtree = self.treeBuilder(element_inorder_location+1, right)
        currentRoot = TreeNode(val = preorder_element, left=leftSubtree, right=rightSubtree)
        return currentRoot
    

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        sz = len(self.preorder)
        for i in range(0,sz): 
            self.inorder_location[inorder[i]] = i
        
        return self.treeBuilder(0, sz-1)
            
            


# 987 https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


#TODO error in this 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.tuple_list = [] 
        
    def dfs(self, node, x, y): 
        if node is None: 
            return 
        self.tuple_list.append(x,-y,node.val)  #need to sort 
        self.dfs(node.left, x-1, y-1)
        self.dfs(node.right, x+1, y-1)
        
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.dfs(root,0,0)
        self.tuple_list.sort()
        sz = len(self.tuple_list)
        ans = [] 
        temp = [] 
        for i in range(0, sz): 
            if i > 0 and not self.tuple_list[i-1][0] == self.tuple_list[i][0]:
                ans.append(temp)
                temp = [] 
            
            temp.append(self.tuple_list[i][2])
        ans.append(temp)
        return ans




### Lecture 1/27/21 
## Trie
# what a trie is: https://github.com/Vikktour/Data-Structures-Algorithms-Implementations/blob/main/1.%20Trie%20-%20converting%20list%20to%20tree%20for%20instant%20access%20to%20targetted%20adjacent%20nodes.py


#208  https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode:
    
    def __init__(self):
        self.links = collections.defaultdict(TrieNode)
        self.endFlag = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        currentNode = self.root
        for ch in word: 
            if ch not in currentNode.links: 
                newNode = TrieNode() 
                currentNode.links[ch] = newNode
            currentNode = currentNode.links[ch]
        currentNode.endFlag = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currentNode = self.root 
        for ch in word: 
            if ch not in currentNode.links: 
                return False
            currentNode = currentNode.links[ch]
        return currentNode.endFlag

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currentNode = self.root 
        for ch in prefix: 
            if ch not in currentNode.links: 
                return False
            currentNode = currentNode.links[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)




#211  https://leetcode.com/problems/design-add-and-search-words-data-structure/


