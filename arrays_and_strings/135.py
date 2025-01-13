class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # greedy solution practice:
        # consider two passes at each index, one from left and one from right
        # check left/right based on if value is less than or greater than current
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            # left pass
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
    
            # "right pass", if value to the right of current exists though, accounting for current element by adding 1 to each candy_count addition
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)