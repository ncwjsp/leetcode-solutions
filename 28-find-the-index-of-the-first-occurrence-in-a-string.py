class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        needle_index = len(needle)
        if needle == haystack:
            return 0
        while i < len(haystack):
            if needle_index <= len(haystack):
                if haystack[i:needle_index] == needle:
                    return i
                elif haystack[i] == needle:
                    return i
            i += 1
            needle_index += 1
        return -1