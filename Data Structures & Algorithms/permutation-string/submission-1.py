class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed-size (len(s1)) sliding window on s2, check if freq of window is equivalent to s1
        if len(s1) > len(s2):
            return False

        freq1 = {}
        freq2 = {}

        # count s1: make frequency dict
        for i in s1: 
            freq1[i] = 1 + freq1.get(i, 0)
            
        for j in range(len(s1)):
            freq2[s2[j]] = 1 + freq2.get(s2[j], 0)

        l = 0
        r = len(s1)

        while r < len(s2):
            if freq1 == freq2: 
                return True

            # Add right character
            freq2[s2[r]] = 1 + freq2.get(s2[r], 0)
            
            # Remove left character
            freq2[s2[l]] -= 1
            if freq2[s2[l]] == 0:
                del freq2[s2[l]]
                
            # Move both pointers forward
            l += 1
            r += 1
            
        # Check the very last window
        return freq1 == freq2



