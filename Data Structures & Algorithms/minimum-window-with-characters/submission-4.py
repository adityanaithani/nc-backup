class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #   return shortest substring of s so:
        # every character in t CONTAINING duplicates is in substring
        # return empty "" if invalid

        # move r until we have every character we need from t
        # move l until the window becomes invalid, record size the whole time
        # repeat until r ends
        # have and need variables

        # IMPLEMENTATION
        if t == "" or len(t) > len(s):
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)

        es = [-1, -1]
        resLen = float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            # add c to window map
            window[c] = 1 + window.get(c, 0)
            # if c is in countT AND count in window matches count in countT, increment have
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                lc = s[l]
                currentLen = r - l + 1

                if currentLen < resLen:
                    resLen = currentLen
                    res = [l, r]

                window[lc] -= 1

                if lc in countT and window[lc] < countT[lc]:
                    have -= 1

                l += 1

        if resLen == float("infinity"):
            return ""
        
        return s[res[0] : res[1] + 1]
 
