class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest = min(strs, key=len)
        
        index = 0
        new_str = ""

        for i in range(len(shortest)):
            new_str += shortest[index]

            for string in strs:
                if string[index] != new_str[index]:
                    return new_str[:-1]

            index += 1

        return new_str