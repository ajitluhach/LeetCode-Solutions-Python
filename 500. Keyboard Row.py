def findWords(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    result = []
    row1 = set("qwertyuiopQWERTYUIOP")
    row2 = set("asdfghjklASDFGHJKL")
    row3 = set("zxcvbnmZXCVBNM")

    for word in words:
        tempword = set(word)
        if tempword <= row1 or tempword <= row2 or tempword <= row3:
            result.append(word)

    return result
