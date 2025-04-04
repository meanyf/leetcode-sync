class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        line = [0] * (2050 - 1950 + 2)
        for start, end in logs:
            line[start - 1950] += 1
            line[end - 1950] -= 1
        m = 0
        cnt = 0
        year = 0
        for i, num in enumerate(line):
            cnt += num
            if m < cnt:
                m = cnt
                year = i + 1950
        return year
        