class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]: return
        rows, cols = len(image), len(image[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        orig = image[sr][sc]
        stack = [(sr, sc)]
        visit = set((sr, sc))
        image[sr][sc] = color
        while stack:
            r, c = stack.pop()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == orig and (nr, nc) not in visit:
                    image[nr][nc] = color
                    stack.append((nr, nc))
                    visit.add((nr, nc))
        return image