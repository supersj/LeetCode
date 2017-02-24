import collections
def minWindow( s, t):
    slist = list(s)
    tlist = list(t)
    stack = []
    minlen = len(slist)
    left = 0
    right = minlen-1
    for i in range(len(slist)):
        needcontinue = False
        if slist[i] in tlist:
            tlist.remove(slist[i])
            stack.append([slist[i], i])
            needcontinue = True
        else:
            for j in range(len(stack)):
                if slist[i] == stack[j][0]:
                    stack.pop(j)
                    stack.append([slist[i], i])
                    needcontinue = True
                    break
        if  needcontinue == True:
            if len(tlist) == 0:
                if minlen > stack[-1][1] - stack[0][1] + 1:
                    minlen = stack[-1][1] - stack[0][1] + 1
                    left = stack[0][1]
                    right = stack[-1][1]
            continue
        if len(tlist) == 0:
            if minlen > stack[-1][1] - stack[0][1] + 1:
                minlen = stack[-1][1] - stack[0][1] + 1
                left = stack[0][1]
                right = stack[-1][1]
            for j in range(len(stack)):
                if slist[i] == stack[j][0]:
                    for t in range(j):
                        tlist.append(stack[t][0])
                    stack[0:j+1] = []
                    stack.append([slist[i], i])
                    break
    if len(tlist) > 0:
        return ""
    if minlen > stack[-1][1] - stack[0][1] + 1:
        left = stack[0][1]
        right = stack[-1][1]
    return s[left:right + 1]

def minWindowII( s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]
s = "ancccddnaoood"

t = "dna"
print(minWindowII(s,t))