class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        item1 = bin(start)[2:][::-1]
        item2 = bin(goal)[2:][::-1]
        print(item1, item2)
        cnt = 0
        i = 0
        for a, b in zip(item1, item2):
            i += 1
            if a != b:
                cnt += 1
        mx_item = []
        if len(item1) != len(item2):
            if len(item1) > len(item2):
                mx_item = item1
            else:
                mx_item = item2
        print(mx_item)
        for j in range(i, len(mx_item)):
            print(mx_item[j])
            if mx_item[j] != '0':
                cnt += 1

        return cnt
