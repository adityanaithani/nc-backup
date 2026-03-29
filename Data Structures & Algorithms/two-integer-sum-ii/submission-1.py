class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted in non-decreasing order
        # two numbers add up to target and idx1 < idx2, also not equal

        # check first number, assume it is idx1, then test values for idx2
        ret = []
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                print(numbers[i], numbers[j])
                if numbers[i] + numbers[j] == target:
                    ret = [i + 1,j + 1]
        return ret