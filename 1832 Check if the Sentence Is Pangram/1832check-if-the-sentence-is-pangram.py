class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        al = "abcdefghijklmnopqrstuvwxyz"
        return len(set(sentence)) == len(al)






