class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # print(set(s))
        if len(list(set(s))) != len(list(set(t))):
            return False
        d = {}
        for i in range(len(s)):
            d[s[i]] = t[i]
        print(d)

        p = ''

        for i in range(len(s)):
            p = p + d[s[i]]

        return p == t

        # s_li = list(s)
        # t_li = list(t)
        # print(s_li,t_li)
        # result = True
        # if len(list(set(s_li))) != len(list(set(t_li))):
        #     return False
        # else:
        #     for i in range(len(s_li)):
        #         if s_li.count(s_li[i])
