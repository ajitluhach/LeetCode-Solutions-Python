class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Solution 1
        """lst = []
        s = s.split(" ")
        for word in s:
            word = word[::-1]
            lst.append(word)
        return ' '.join(lst)
        """
        # Solution 2

        """

        return ' '.join(map(lambda x: x[::-1], s.split()))

        """
        # Solution 3
        def split(string):
            words = []
            word = ''
            for x in string:
                if x == ' ':
                    words.append(word)
                    word = ''
                else:
                    word += x
            words.append(word)
            return words

        def reverse(string):
            if len(string) <= 1:
                return string
            return reverse(string[1:]) + string[0]
        res = []
        s = split(s)
        for word in s:
            w = reverse(word)
            res.append(w)
        return ' '.join(res)
