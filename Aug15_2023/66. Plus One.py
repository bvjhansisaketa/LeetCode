class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 0
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits)-1:
                if digits[i]+1 < 10:
                    digits[i]=digits[i]+1
                    c = 0
                else:
                    if i ==0:
                        digits[i]=0
                        digits.insert(0,1)
                    else:
                        digits[i]=0
                        c = 1
            else:
                if c ==0:
                    digits[i]=digits[i]
                else:
                    if digits[i]+c < 10:
                        digits[i]=digits[i]+1
                        c = 0
                    else:
                        if i ==0:
                            digits[i]=0
                            digits.insert(0,1)
                        else:
                            digits[i]=0
                            c = 1
        return(digits)

        # if digits[len(digits)-1]<9:
        #     digits[len(digits)-1]= digits[len(digits)-1]+1
        # else:
        #     if len(digts)
