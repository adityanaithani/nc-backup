class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find length of longest substring without duplicate chars
        # use set() for the duplicate check
        # order matters, so sliding window until set check fails, then move l ptr

        subset = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            # if we find a duplicate
            while s[r] in subset:
                # remove character at l and move l forward - shrinking window
                subset.remove(s[l])
                l += 1
        # now can expand and add new char to the set, update longest
            subset.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

