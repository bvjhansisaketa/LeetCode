class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        string = s.split(' ')
        print(p,string)
        print(len(p),len(string))
        d = {}
        if len(set(p)) != len(set(string)) or len(p)!=len(string):
            return False
        for i in range(len(string)):
            d[p[i]] = string[i]
        for i in range(len(string)):
            p[i]=d[p[i]]
        print(p,string)
        return string == p
