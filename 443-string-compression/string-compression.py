#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        prev = chars[0]
        cnt = 1
        insert = 0
        for i in range(1, len(chars)):
            ans = chars[i]
            if chars[i] == prev:
                cnt += 1
            else:
                chars[insert] = prev
                insert += 1
                if cnt > 1:
                    cnt_list = list(str(cnt))
                    for i in range(len(cnt_list)):
                        chars[i + insert] = cnt_list[i]
                    insert += len(cnt_list)
                cnt = 1
            prev = ans
        chars[insert] = prev
        insert += 1
        if cnt > 1:
            cnt_list = list(str(cnt))
            for i in range(len(cnt_list)):
                chars[i + insert] = cnt_list[i]
            insert += len(cnt_list)
        
        return insert
# @lc code=end

