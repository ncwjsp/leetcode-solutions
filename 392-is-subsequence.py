class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        sIndex = 0

        if s == "":
            return True

        for i in range(tLen):
            if s[sIndex] == t[i]:
                if sIndex == sLen - 1:
                    return True
                sIndex += 1

        return False