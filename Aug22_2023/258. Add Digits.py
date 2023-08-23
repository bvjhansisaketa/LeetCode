#10 mins
class Solution:
    def addDigits(self, num: int) -> int:
        r = num
        while(len(str(r))!=1):
            x = 0
            for i in str(r):
                x = x + int(i)
            r = x
        return(r)