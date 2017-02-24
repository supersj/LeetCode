class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = ["+","-","*","/"]
        stack = []
        for ele in tokens:
            if ele in operators:
                a = stack.pop()
                b = stack.pop()
                if ele == "+":
                    stack.append(a + b)
                elif ele == "-":
                    stack.append(b - a)
                elif ele == "*":
                    stack.append(a * b)
                else:
                    # TODO no renosense 
                    positive = 1
                    if a*b < 0:
                        positive = -1
                    stack.append((abs(b) // abs(a))*positive)
            else:
                stack.append(int(ele))
        return stack[-1]

hh =Solution()
nums = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(hh.evalRPN(nums))