#!/bin/python2
# -*- coding:utf-8 -*-

class Solution:
    # @return an integer
    romans = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    def romanToInt(self, s):
        def _singleint(i):
            return self.romans[s[i]]

        num = 0
        for i in xrange(len(s) - 1):
            num += _singleint(i) * (-1 if _singleint(i) < _singleint(i+1) else 1)

        return num + _singleint(-1)


if __name__ == "__main__":
    import sys
    sol = Solution()
    print(sol.romanToInt(sys.argv[1]))
