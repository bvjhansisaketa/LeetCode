class Solution:
    def hammingWeight(self, n: int) -> int:
        n = format(n, 'b')
        k = 0
        print(n)
        print(str(n))
        for i in str(n):
            if i == '1':
                print(i)
                k = k + 1
        return (k)
