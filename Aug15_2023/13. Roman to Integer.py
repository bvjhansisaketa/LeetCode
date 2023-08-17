class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        # I,V,X,L,C,D,M,IV,IX,XL,XC,CD,CM
        i = 0
        while (i<len(s)):
            if s[i] == 'I':
                if i != len(s)-1:
                    if s[i+1]=='V':
                        integer = integer + 4
                        i = i + 1
                    elif s[i+1] == 'X':
                        integer = integer + 9
                        i = i + 1
                    else:
                        integer = integer + 1
                else:
                    integer = integer + 1
            elif s[i] == 'V':
                integer = integer + 5
            elif s[i] == 'X':
                if i != len(s)-1:
                    if s[i+1]=='L':
                        integer = integer + 40
                        i = i + 1
                    elif s[i+1] == 'C':
                        integer = integer + 90
                        i = i +1
                    else:
                        integer = integer + 10
                else:
                    integer = integer + 10
            elif s[i] == 'L':
                integer = integer + 50
            elif s[i] == 'C':
                if i != len(s)-1:
                    if s[i+1]=='D':
                        integer = integer + 400
                        i = i +1
                    elif s[i+1] == 'M':
                        integer = integer + 900
                        i = i + 1
                    else:
                        integer = integer + 100
                else:
                    integer = integer + 100
            elif s[i] == 'D':
                integer = integer + 500
            elif s[i] == 'M':
                integer = integer + 1000
            i = i + 1
        return(integer)

