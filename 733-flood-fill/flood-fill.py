class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        rows, cols = len(image), len(image[0])
        stack = [(sr, sc)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        while stack:
            i, j = stack.pop()
            visited.add((i, j))
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if (ni, nj) in visited:
                    continue
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                    continue
                if image[i][j] == image[ni][nj]:
                    stack.append((ni, nj))
            image[i][j] = color
        return image