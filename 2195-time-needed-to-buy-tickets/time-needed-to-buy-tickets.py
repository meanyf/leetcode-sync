class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(tickets)
        t = 0
        while tickets:
            if tickets[k] == 1 and k == 0:
                return t + 1
            tickets[0] -= 1
            if tickets[0] > 0:
                tickets.append(tickets[0])
            t += 1
            tickets.popleft()
            k -= 1
            if k < 0:
                k = len(tickets) - 1
        return t