#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
	def countBinarySubstrings(self, s: str) -> int:
		n = len(s)
		cnt = 0
		zerofist = onesFisr = False
		if s[0] == '0': zerofist = True
		else: onesFisr = True
		zeros = 0
		ones = 0
		for i in range(n):
			if zerofist and s[i] == '0' and ones != 0:
				zerofist = False
				onesFisr = True
				cnt += min(ones, zeros)
				zeros = 0
			if onesFisr and s[i] == '1' and zeros != 0:
				zerofist = True
				onesFisr = False
				cnt += min(ones, zeros)
				ones = 0
			if s[i] == '0':
				zeros += 1
			elif s[i] == '1':
				ones += 1
		cnt += min(ones, zeros)
		return cnt
# @lc code=en

