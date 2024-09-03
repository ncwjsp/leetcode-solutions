class Solution:
    def romanToInt(self, s: str) -> int:
        rmVal = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        r = list(reversed(s))
        val = 0
        prev = 0
        for i in r:
            current = rmVal[i]
            # subtract when current value is less than the previous value
            if prev > current:
                val -= current
            else:
                val += current
            prev = current
        return val
