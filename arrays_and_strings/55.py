class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # get length of list, aka number of steps required to reach the last index
        n = len(nums)
        current_pos = 0

        while current_pos < n - 1:
            max_jump = 0
            next_pos = current_pos # next position we jump to
            for i in range(1, nums[current_pos] + 1):
                #find max jump based on current element, update current pos
                if current_pos + i >= n:
                    return True
                if current_pos + i + nums[current_pos + i] > max_jump:
                    max_jump = current_pos + i + nums[current_pos + i]
                    next_pos = current_pos + i
            if next_pos == current_pos:
                return False
            current_pos = next_pos

        return True

        

        