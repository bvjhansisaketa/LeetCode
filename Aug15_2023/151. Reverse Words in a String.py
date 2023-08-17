class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(' ')
        print(li)

        reverse = ''
        for i in range(len(li)-1,-1,-1):
            if li[i] != '':
                reverse = reverse + li[i] + ' '
        return(reverse[0:len(reverse)-1])

