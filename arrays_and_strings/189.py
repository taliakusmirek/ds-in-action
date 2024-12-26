# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Get length of list
        n = len(nums)
        # Figure out how many spots each value rotates based on length of list
        k = k % n
        # Reverse the list
        nums.reverse()
        # The values that would go "over" the list are reversed at the beginning of the list
        nums[:k] = reversed(nums[:k])
        # The value that don't go "over the list" stay in the list but get reversed to be in ascending order
        nums[k:] = reversed(nums[k:])