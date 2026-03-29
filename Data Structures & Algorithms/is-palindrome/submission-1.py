class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove case, spaces
        # remove non-alphanumeric
        sanitized = re.sub(r'[^a-zA-Z0-9]', '', s.replace(" ", "").lower())
        return sanitized == sanitized[::-1]
