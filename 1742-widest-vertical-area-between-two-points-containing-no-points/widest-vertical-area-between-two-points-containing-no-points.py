class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        mx = 0
        for i in range(len(points) - 1):
            mx = max(mx, abs(points[i][0] - points[i + 1][0]))
        return mx