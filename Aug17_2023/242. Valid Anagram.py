class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s))!=len(set(t)) or set(s)!=set(t) or len(s)!=len(t):
            return False
        else:
            result = True
            for i in range(len(s)):
                if s.count(s[i]) != t.count(s[i]):
                    result = False
            return result