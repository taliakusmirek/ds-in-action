class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # sort using insertion sort
        n = len(citations)
        for i in range(1, n):
            j = i - 1
            temp = citations[i]
            while (j >= 0 and citations[j] > temp):
                citations[j + 1] = citations[j]
                j -= 1
            citations[j + 1] = temp
        
        # reverse sorted list to be in descending order
        reversed_l = citations[::-1]

        # h-index is the index i such that citations[i] >= i + 1
        h = 0 # counter for number of citations 
        for i in range(0, n):
            if reversed_l[i] >= i + 1: # if current citation amount exceeds our previous recorded number of possible citations
                h = i + 1 # increment number of possible citations by 1
            # if the if statement is false, we have found the limit of possible citations
        return h
        

        