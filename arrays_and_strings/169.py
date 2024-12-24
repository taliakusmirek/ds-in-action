# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Calculate majority value, n/2 based on list length
        majority_threshold = len(nums) / 2
        # Create a dictionary using the elements as the key
        counts = {}
        # Iterate through list, adding 1 to element count in dictionary
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        # For each pair in dictionary, if its count is greater than majority value set that pairs key (the element) as our majority
        majority_val = 0
        for num, count in counts.items():
            if count > majority_threshold:
                majority_val = num
        # Return majority element
        return majority_val
        