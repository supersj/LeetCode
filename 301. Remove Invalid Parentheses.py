from queue import *
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def cnt(s):
            stack = []
            for e in s:
                if e[0] != '(' and e[0] != ')':
                    continue
                if not stack:
                    stack.append(e[0])
                    continue
                if e == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(e[0])
            return len(stack)
        def isvalid(s):
            count = 0
            for i in range(len(s)):
                c = s[i]
                if c == '(':
                    count += 1
                if c == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0
        res = []
        if not s:
            return [""]
        visited = set()
        q = Queue()
        q.put(s)
        visited.add(s)
        found = False
        while not q.empty():
            s = q.get()
            if isvalid(s):
                res.append(s)
                found = True
            if found:
                continue
            for i in range(len(s)):
                if s[i] not in ['(',')']:
                    continue
                t = s[0:i] + s[i+1:]
                if t not in visited:
                    visited.add(t)
                    q.put(t)
        return res

class Solution1(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def cnt(s):
            stack = []
            for e in s:
                if e not in ['(',')']:
                    continue
                if not stack:
                    stack.append(e)
                    continue
                if e == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(e)
            return len(stack)
        def isvalid(s):
            count = 0
            for i in range(len(s)):
                c = s[i]
                if c == '(':
                    count += 1
                if c == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0
        def helper(s,result,count,visited):
            if count == 0:
                return
            for i in range(len(s)):
                if s[i] != '(' and s[i] != ')':
                    continue
                tmp = s[:i] + s[i+1:]
                if tmp in visited:
                    continue
                visited.add(tmp)
                c = cnt(tmp)
                if c != count - 1:
                    continue
                if count == 1:
                    if isvalid(tmp):
                        result.append(tmp)
                if count > 1:
                    helper(tmp, result, count-1,visited)
        if not s:
            return [""]
        res = []
        c = cnt(s)
        if c == 0:
            return [s]
        visited = set()
        helper(s,res,c,visited)
        return res
s = ")(())((((()("
hh = Solution1()
print(hh.removeInvalidParentheses(s))