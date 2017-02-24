def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    wordslen = len(words)
    result = []
    i = 0
    while i < wordslen:
        start = i
        last = i
        tmplength = len(words[i])
        tmpresult = words[i]
        for j in range(i + 1, wordslen):
            tmplength += len(words[j]) + 1
            last += 1
            if tmplength > maxWidth:
                tmplength -= len(words[j]) + 1
                last -= 1
                break
        linenumbers = last - start + 1
        if linenumbers == 1:
            tmpresult += ' ' * (maxWidth - tmplength + linenumbers - 1)
            result.append(tmpresult)
            i = last +1
            continue
        a, b = divmod(maxWidth - tmplength + linenumbers-1, linenumbers-1)
        if last == wordslen - 1:
            for j in range(linenumbers - 1):
                tmpresult = tmpresult + ' ' + words[start + 1 + j]
            tmpresult = tmpresult+ ' '*(maxWidth - len(tmpresult))
            result.append(tmpresult)
            return result
        for j in range(linenumbers - 1):
            if b > 0:
                tmpresult = tmpresult + ' '
                b -= 1
            tmpresult +=' ' * a + words[start + 1 + j]
        i = last + 1
        result.append(tmpresult)
    return result


words =  ["This", "is", "an", "example", "of", "text", "justi.","aa"]
print(fullJustify(words,16))