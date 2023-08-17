class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minP = prices[0]
        # minIndex = 0
        # for i in range(len(prices)):
        #     if prices[i] < minP:
        #         minP = prices[i]
        #         minIndex = i
        # print(minP,minIndex)

        # maxP = prices[minIndex]
        # maxIndex = minIndex
        # for i in range(minIndex,len(prices)):
        #     if prices[i] > maxP:
        #         maxP = prices[i]
        #         maxIndex = i
        # print(maxP,maxIndex)
        # return maxP - minP

        # l = []

        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         l.append(prices[j]-prices[i])
        # return(max(l))

        l = 0
        r = 1
        maxP = 0
        while r < len(prices):
            curP = prices[r] - prices[l]
            # print("left and right prices",prices[l],prices[r])
            if prices[l] < prices[r]:
                # print(maxP,curP)
                maxP = max(curP, maxP)

            else:
                l = r
            r = r + 1
        return maxP

