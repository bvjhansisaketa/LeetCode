class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l = l + 1
            r = r + 1

        if l == len(s):
            return True
        else:
            return False
        # print(t.rindex('a'))
        # if s=='':
        #     return True
        # l = list(s)
        # result = True
        # print(l)
        # for i in l:
        #     print(i,t.find(i))
        #     if t.find(i) == -1:
        #         result = False
        #         return result

        # lastIndex = t.index(l[0])
        # for i in range(0,len(l)):
        #     if lastIndex <= t.index(l[i]) and t.count(l[i])==1:
        #         lastIndex = t.index(l[i])
        #     else:
        #         result = False
        #         return result
        # return result

        return (result)