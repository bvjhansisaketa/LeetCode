class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')

        r = ''

        for i in range(len(l)-1,-1,-1):
            if l[i]!='':
                r = r + l[i] + ' '
        return(r[0:len(r)-1])