class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        rows, cols = len(image), len(image[0])
        stack = [(sr, sc)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        original_color = image[sr][sc]
        if original_color == color:
            return image
        while stack:
            i, j = stack.pop()
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                    continue
                if original_color == image[ni][nj]:
                    stack.append((ni, nj))
            image[i][j] = color
        return image