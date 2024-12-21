# You are given two integer arrays, nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums 2 respectively.



# Goal: Merge nums1 and nums2 into a single array sorted in non-decreasing order (ascending order).

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int, number of elements in nums1
        :type nums2: List[int]
        :type n: int, number of elements in nums2
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
    

        # Add nums2 elements to nums1 to have a single array to sort
        for i in range(n):
            nums1[m + i] = nums2[i]        
        #print(nums1) # Check nums1 has all of nums2 elements before sorting...

        # Insertion Sort all of nums1! This takes O(n^2) time.
        i = 1
        y = m + n
        for i in range(y):
            j = i - 1
            temp = nums1[i]
            while (j >= 0 and temp <= nums1[j]):
                nums1[j + 1] = nums1[j]
                j -= 1
            nums1[j + 1] = temp # Remember to do j+1 and not just j, j+1 = i!
        
        #print(nums1) # Check nums1 is a sorted ascending list of the merged elements of nums1 and nums2
        