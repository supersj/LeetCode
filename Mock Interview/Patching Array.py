# todo too hard to work out an amazing solution
class Solution1(object):
    def minPatches(self, nums, n):
        miss,added,i = 1,0,0
        while miss <= n:
            if i<len(nums) and nums[i] <= miss:
                miss += nums[i]
                i+=1
            else:
                miss += miss
                added += 1
        return added
    def minPatches1(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        remain = set([i for i in range(1,n+1)])
        fit = set([])
        tmp = set()
        for num in nums:
            tmp.clear()
            tmp.add(num)
            for i in fit:
                tmp.add(i+num)
            remain = remain - tmp
            fit = fit.union(tmp)
            if not remain:
                return 0
        count = 0
        while remain:
            count += 1
            num = min(remain)
            tmp.clear()
            tmp.add(num)
            for i in fit:
                tmp.add(i+num)
            remain = remain - tmp
            fit = fit.union(tmp)
        return count
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        def merge(left,num):
            right = [[num, num]]
            for ele in left:
                right.append([ele[0] + num, ele[1] + num])
            stack = []
            i,j,ll,lr = 0,0,len(left),len(right)
            while i<ll and j <lr:
                if left[i][0] <= right[j][0]:
                    if not stack:
                        stack.append(left[i])
                    else:
                        if left[i][0] <= stack[-1][1] + 1:
                            stack[-1][1] = max(stack[-1][1],left[i][1])
                        else:
                            stack.append(left[i])
                    i+=1
                else:
                    if not stack:
                        stack.append(right[j])
                    else:
                        if right[j][0] <= stack[-1][1] + 1:
                            stack[-1][1] = max(stack[-1][1],right[j][1])
                        else:
                            stack.append(right[j])
                    j+=1
            if i < ll:
                while i < ll:
                    if not stack:
                        stack.append(left[i])
                    else:
                        if left[i][0] <= stack[-1][1] + 1:
                            stack[-1][1] = max(stack[-1][1],left[i][1])
                        else:
                            stack.append(left[i])
                    i+=1
            if j < lr:
                while j < lr:
                    if not stack:
                        stack.append(right[j])
                    else:
                        if right[j][0] <= stack[-1][1] + 1:
                            stack[-1][1] = max(stack[-1][1],right[j][1])
                        else:
                            stack.append(right[j])
                    j+=1
            return stack
        stack = []
        for num in nums:
            if not stack:
                stack.append([num,num])
            else:
                stack = merge(stack,num)
        cnt = 0
        if not stack:
            cnt += 1
            stack = [[1,1]]
        while stack[0][0] != 1 or stack[0][1] < n:
            cnt += 1
            if stack[0][0] == 1:
                num = stack[0][1] + 1
            else:
                num = 1
            if not stack:
                stack.append([num,num])
            else:
                stack = merge(stack,num)
        return cnt

nums = [145,186,220,317,320,354,374,386,396,406,504,512,528,596,631,634,668,675,706,715,728,771,777,778,804,878,940,973,975,998,1048,1082,1089,1130,1137,1144,1155,1206,1238,1319,1333,1345,1357,1358,1408,1436,1479,1485,1486,1510,1521,1565,1581,1614,1635,1649,1674,1676,1684,1732,1776,1812,1879,1886,1888,1900,1904,1985,2000,2012,2020,2054,2061,2084,2135,2210,2231,2238,2249,2269,2295,2308,2310,2342,2348,2356,2357,2458,2492,2537,2644,2663,2667,2670,2704,2705,2770,2788,2834,2841,2868,2890,2902,2905,2948,3010,3024,3056,3065,3067,3106,3115,3116,3125,3126,3130,3158,3181,3193,3210,3224,3251,3283,3329,3398,3417,3435,3436,3447,3449,3474,3476,3479,3496,3519,3541,3602,3629,3644,3685,3704,3713,3751,3757,3772,3799,3847,3897,3942,3958,3961,3981,4001,4014,4022,4024,4029,4056,4059,4067,4069,4069,4099,4105,4118,4120,4137,4138,4177,4183,4205,4209,4214,4216,4228,4253,4294,4301,4402,4422,4458,4467,4479,4482,4489,4520,4544,4581,4688,4699,4706,4730,4805,4807,4860,4868,4872,4875,4890,4941,4948,4949,4959,4968,5077,5092,5128,5151,5165,5195,5231,5334,5350,5353,5397,5439,5445,5466,5467,5501,5558,5574,5577,5639,5664,5704,5711,5747,5837,5851,5876,5881,5911,5916,5925,5929,5964,5970,6012,6101,6104,6113,6116,6129,6137,6147,6147,6184,6205,6215,6218,6229,6292,6315,6348,6349,6350,6352,6353,6364,6371,6423,6436,6450,6490,6508,6593,6621,6655,6662,6696,6708,6710,6732,6732,6776,6788,6816,6820,6825,6830,6862,6862,6872,6892,6923,6995,7022,7091,7098,7122,7138,7151,7155,7195,7237,7243,7277,7351,7358,7370,7378,7396,7402,7405,7411,7468,7472,7497,7506,7511,7543,7659,7680,7684,7734,7758,7759,7775,7792,7797,7799,7827,7834,7836,7861,7877,7893,7903,7918,7983,7983,8000,8053,8080,8115,8119,8137,8179,8180,8209,8224,8255,8276,8284,8311,8415,8447,8452,8500,8506,8523,8583,8597,8645,8654,8675,8684,8694,8696,8715,8719,8755,8809,8819,8838,8856,8898,8949,8984,9042,9091,9103,9132,9175,9186,9249,9271,9327,9328,9340,9379,9429,9512,9519,9577,9608,9621,9653,9688,9711,9722,9741,9746,9782,9837,9859,9916,9950,9954]
n = 2147483647
# n = 54
hh = Solution()
hh.minPatches(nums,n)