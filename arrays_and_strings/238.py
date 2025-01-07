class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        # for each element in nums
        # skip and multiply and put into a sum and then store in answer, via a for loop 
        # note: to account for "wrap around", a two pass approach works without division
        for i in range(len(nums)):
            total = 1
            # two pass approach, first from left of element, second from right of element      
            for j in range(i):
                total *= nums[j]
            for z in range(i + 1, len(nums)):
                total *= nums[z]
            answer.append(total)
        return answer