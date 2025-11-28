# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        while True:
            a = rand7()  # 1-7
            b = rand7()  # 1-7
            c = rand7()  # 1-7
            
            num = (a - 1) * 49 + (b - 1) * 7 + c  # 1-343
            
            if num <= 340:
                return (num - 1) % 10 + 1