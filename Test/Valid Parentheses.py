class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        p = {')':'(','}':'{',']':'['}
        for i in s:
            if i in p and len(l)>0:
                if l[len(l)-1] != p[i]:
                    break
                l.pop()
            else:
                l.append(i)
                # print(l)

        return(len(l)==0)