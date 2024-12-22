# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        k = 1 # first element is always unique
        for i in range(1, len(nums)):
            j = i - 1
            if nums[j] != nums[i]: # two unique ints
                nums[k] = nums[i]
                k += 1
                print(nums)
        return k
        