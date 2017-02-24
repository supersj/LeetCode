# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ratingsLen = len(ratings)
        left = [1 for i in range(ratingsLen)]
        right = [1 for i in range(ratingsLen)]
        result = 0
        for i in range(1,ratingsLen):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
            if ratings[ratingsLen-i-1] > ratings[ratingsLen-i]:
                right[ratingsLen-i-1] = right[ratingsLen-i] + 1
        for i in range(0,ratingsLen):
            result += max(left[i],right[i])
        return result