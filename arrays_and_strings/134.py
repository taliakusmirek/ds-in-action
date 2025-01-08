class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_g = 0
        total_c = 0
        tank = 0
        starting = 0
        # look at station, gas[i], is tank - cost[i] > 0? if so continue iterating with a inner for loop, including wrap around, else move i+1 to consider the next possible station
        for i in range(len(gas)):
            total_g += gas[i]
            total_c += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                starting = i + 1
        # if the cost is more than the total gas we have.... return -1, else return starting point that works
        if total_c > total_g:
            return -1
        return starting