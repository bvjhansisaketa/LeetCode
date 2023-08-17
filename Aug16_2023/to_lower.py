class Solution:
    def toLowerCase(self, s: str) -> str:
        for i in s:
            if 65<=ord(i)<=90:
                s = s.replace(i,chr(ord(i)+32))
        return(s)