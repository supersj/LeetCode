# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# Note: Do not use the eval built-in library function.
#
# Subscribe to see which companies asked this questio

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
            elif s[i] == '(':
                stack.append(s[i])
                i += 1
            elif s[i] == '+' or s[i] == '-':
                stack.append(s[i])
                i += 1
            else:
                sum = 0
                i += 1
                while True:
                    num1 = stack.pop()
                    op = stack.pop()
                    if op == '+':
                        sum += num1
                    elif op == '-':
                        sum -= num1
                    else:
                        sum += num1
                        break
                stack.append(sum)
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

hh = Solution()
s = "11+ 1 -(1 + 2)"
hh.calculate(s)