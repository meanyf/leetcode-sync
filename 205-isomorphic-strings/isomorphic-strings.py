class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        st = set()
        for a, b in zip(s, t):
            if a in d:
                if d[a] != b:
                    return False
            else:
                if b in st:
                    return False
                d[a] = b
            st.add(b)
        return True