# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.
#
# Subscribe to see which companies asked this question

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gaslen = len(gas)
        for i in range(gaslen):
            gas[i] = gas[i] - cost[i]
        gas = gas*2
        start = 0
        begin = 0
        end = start + gaslen
        tmpgas = 0
        while begin != end and start<gaslen:
            tmpgas += gas[begin]
            if tmpgas < 0:
                end = end + begin - start + 1
                start = begin + 1
                tmpgas = 0
            begin += 1
        if start >= gaslen:
            return -1
        return start

"""
I have thought for a long time and got two ideas:

If car starts at A and can not reach B. Any station between A and B
can not reach B.(B is the first station that A can not reach.)
If the total number of gas is bigger than the total number of cost. There must be a solution.
(Should I prove them?)
Here is my solution based on those ideas:

class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int start(0),total(0),tank(0);
        //if car fails at 'start', record the next station
        for(int i=0;i<gas.size();i++) if((tank=tank+gas[i]-cost[i])<0) {start=i+1;total+=tank;tank=0;}
        return (total+tank<0)? -1:start;
    }
};
"""

hh = Solution()
gas = [2,4]
cost = [3,4]
hh.canCompleteCircuit(gas,cost)