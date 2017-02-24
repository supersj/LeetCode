class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        s = '#' + s
        i = 1
        stack.append('#')
        lens = len(s)
        while i < lens:
            if s[i] == ' ':
                i += 1
                continue
            elif '0' <= s[i] <= '9':
                tmp = ''
                while  i<lens and '0' <= s[i] <= '9' :
                    tmp += s[i]
                    i += 1
                stack.append(int(tmp))
            elif s[i] == '*' or s[i] == '/':
                op = s[i]
                num1 = stack.pop()
                i += 1
                while s[i] == ' ':
                    i+= 1
                tmp = ''
                while i < lens and '0' <= s[i] <= '9':
                    tmp += s[i]
                    i += 1
                num2 = int(tmp)
                if op == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(num1 // num2)
            else:
                stack.append(s[i])
                i += 1
        sum = 0
        while stack:
            num1 = stack.pop()
            op = stack.pop()
            if op == '+':
                sum += num1
            elif op == '-':
                sum -= num1
            else:
                sum += num1
                break
        return sum
s = " 3+5 / 2 "
hh = Solution()
hh.calculate(s)