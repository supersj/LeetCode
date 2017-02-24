class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        def diffHelp(operand,operator):
            result = []
            if not operator:
                return operand
            for i in range(len(operator)):
                left = diffHelp(operand[0:i+1],operator[0:i])
                right = diffHelp(operand[i+1:],operator[i+1:])
                for l in left:
                    for r in right:
                        tmp = 0
                        if operator[i] == '*':
                            tmp = l * r
                        elif operator[i] == '-':
                            tmp = l - r
                        else:
                            tmp = l + r
                        result.append(tmp)
            return result
        operand = []
        operator = []
        if not input:
            return []
        start = 0
        nlen = len(input)
        while start < nlen:
            if '0' <= input[start]<= '9':
                tmp = ""
                tmp += input[start]
                start += 1
                while start< nlen and '0' <= input[start]<= '9':
                    tmp += input[start]
                    start += 1
                operand.append(int(tmp))
            else:
                operator.append(input[start])
                start += 1
        result = diffHelp(operand,operator)
        return result
hh = Solution()
hh.diffWaysToCompute('2-1-1')