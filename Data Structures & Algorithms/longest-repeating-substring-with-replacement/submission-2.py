class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}
        l = 0
        max_freq = 0
        longest = 0

        for r in range(len(s)):
            # add s[r] to dictionary / update counts in dict and longest
            freq[s[r]] = 1 + freq.get(s[r], 0)

            # update max_freq
            max_freq = max(max_freq, freq[s[r]])

            # check if window is valid
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            # calculate longest
            longest = max(longest, r - l + 1)
        return longest