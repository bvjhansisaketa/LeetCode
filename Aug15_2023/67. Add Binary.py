class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 1 + 0 = 1
        # 0 + 0 = 0
        # 1 + 1 = 10
        # 0 + 1 = 1

        l = max(len(a), len(b))
        if len(a) < len(b):
            a = '0' * (l - len(a)) + a
        else:
            b = '0' * (l - len(b)) + b
        print(a, b)

        c = ''
        cr = 0
        for i in range(l - 1, -1, -1):
            if a[i] == '0' and b[i] == '0':
                if cr == 0:
                    c = c + '0'
                else:
                    c = c + '1'
                    cr = 0
            elif a[i] == '0' and b[i] == '1' or a[i] == '1' and b[i] == '0':
                if cr == 0:
                    c = c + '1'
                else:
                    if i != 0:
                        c = c + '0'
                        cr = 1
                    else:
                        c = c + '01'
            elif a[i] == '1' and b[i] == '1':
                if cr == 0:
                    if i != 0:
                        c = c + '0'
                        cr = 1
                    else:
                        c = c + '01'
                else:
                    if cr == 1:
                        if i != 0:
                            c = c + '1'
                            cr = 1
                        else:
                            c = c + '11'

        return (c[::-1])
