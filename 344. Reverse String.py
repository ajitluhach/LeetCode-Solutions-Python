class Solution(object):
    def reverseString(self, string):
        """
        :type string: str
        :rtype: str
        """
        # if len(string) <= 0:
        #     return ''
        # Generate recursion limit exceeded, couldn't be accepted
        # return self.reverseString(string[1:]) + string[0]
        lst = list(string)
        return ''.join([lst[i - 1] for i in range(len(lst), 0, -1)])

class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        # Solve recursion in binary way. O(logn)
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])


class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        # a beautiful way to do it. maintain a lower index and higher index, increase the lower index and decrease the higher index, swap them. 
        # they will conver at a point
        # should be O(logn)

        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

class SolutionPythonic(object):
    def reverseString(self, s):
        # A move pythonic soution to the problem
        return s[::-1]
