class Solution:
    def strrev(x):
        return x[::-1]
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = -1* x
        rev = int(str(x)[::-1])
        if neg:
            rev = -1*rev
        if rev >= -2**31 and rev < 2**31:
            return rev
        else:
            return 0