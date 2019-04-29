class Solution:
    def reverse(self, x: int) -> int:
        minus = False
        if x < 0:
            minus = True
            x = -x
        if x == 0:
            return x
        y = 0
        while x > 0:
            y = y*10 + x % 10
            x = x//10
        if minus and y<= 1<<31:
            return -y
        elif y< 1<<31:
            return y
        else:
            return 0
