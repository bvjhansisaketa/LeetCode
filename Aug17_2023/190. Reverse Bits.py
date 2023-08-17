class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        s = format(n,'b')
        if len(s) < 32:
            s = str(0)*(32-len(s)) + s
        print(s)
        return(int(s[::-1],2))