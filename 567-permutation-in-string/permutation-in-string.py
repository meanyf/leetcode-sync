class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2 or len(s2) < len(s1):
            return False
        d = {}
        window = {}
        for item in s1:
            d[item] = d.get(item, 0) + 1
        l = 0
        for r, ch in enumerate(s2):
            window[ch] = window.get(ch, 0) + 1
            
            
            while window[ch] > d.get(ch, 0):
                if s2[l] in window:
                    window[s2[l]] -= 1
                l += 1
                
            if r - l + 1 == len(s1):
                return True
            

            
        return False
        

        