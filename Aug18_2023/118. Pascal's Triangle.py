class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []
        for i in range(numRows):
            row = [None] * (i + 1)
            row[0] = 1
            row[-1] = 1

            for j in range(1, len(row) - 1):
                row[j] = l[i - 1][j - 1] + l[i - 1][j]

            # print(l)
            print(row)

            l.append(row)

        return (l)