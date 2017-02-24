def tolist(neted):
    result = []
    for i in range(len(neted)):
        if neted[0] == '*':
            result.append('*')
        else:
            result.extend(tolist(neted[i]))
    return result
neted = [['*','*'],'*',['*','*']]
result = tolist(neted)
print(result)
