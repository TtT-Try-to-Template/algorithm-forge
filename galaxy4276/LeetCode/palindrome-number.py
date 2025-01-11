def rev(s: str) -> str:
    ret = [None] * len(s)
    c = 0
    for i in range(len(s), 0, -1):
        ret[c] = s[i - 1]
        c += 1
    return ''.join(ret)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        r = rev(s)
        return r == s
