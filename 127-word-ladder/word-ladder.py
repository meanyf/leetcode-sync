class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        endWords = set(wordList)
        if endWord not in endWords:
            return 0
        visited = set([beginWord])
        q = deque()
        q.append((beginWord, 1))
        differ_by_one = lambda cur, item: len(cur) == len(item) and sum(a != b for a, b in zip(cur, item)) == 1
        while q:
            cur, dist = q.popleft()
            if cur == endWord:
                return dist
            for i, ch in enumerate(cur):
                for j in range(ord('a'), ord('z') + 1):
                    if ch != chr(j):
                        item = cur[:i] + chr(j) + cur[i+1:]
                        if item in visited:
                            continue
                        if item in endWords:
                            q.append((item, dist + 1))
                            visited.add(item)
                
        return 0
