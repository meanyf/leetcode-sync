class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [item for item in order if item in set(friends)]