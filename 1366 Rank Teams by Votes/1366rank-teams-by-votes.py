class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        d = {}
        length = len(votes[0])
        
        for i, s in enumerate(votes[0]):
            d[s] = [0] * length

        for vote in votes:
            for i, s in enumerate(vote):
                d[s][i] = d.get(s, 0)[i] + 1

        lst = sorted(d.items(), key=lambda x: ([-v for v in x[1]], x[0]))

        return ''.join([x[0] for x in lst])