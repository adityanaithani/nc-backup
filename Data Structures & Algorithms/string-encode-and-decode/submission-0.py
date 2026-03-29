class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            fragment = f"{len(s)}#{s}"
            encoded += fragment
        return encoded

    def decode(self, s: str) -> List[str]:
        # recieve string encoded like 5#Hello5#World
        # read numbers until first #
        # then jump forward [num] chars and slice the string
        # add it to output array

        i = 0
        length = 0
        fragment = ""
        decoded = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            fragment = s[j + 1 : j + 1 + length]
            print(fragment)
            decoded.append(fragment)
            i = j + 1 + length
        
        print(decoded)
        return decoded