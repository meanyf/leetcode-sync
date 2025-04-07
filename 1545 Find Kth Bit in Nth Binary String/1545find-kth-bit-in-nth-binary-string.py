class Solution(object):
    def findKthBit(self, n, k):
        def invert_bits(binary_string):
            return ''.join('1' if bit == '0' else '0' for bit in binary_string)
        memo = {}
        def m(n):
            if n in memo:
                return memo[n]
            if n <= 0:
                return '0'
            memo[n] = m(n - 1) + '1' + invert_bits(m(n - 1))[::-1]
            return memo[n]
        return m(n)[k - 1]