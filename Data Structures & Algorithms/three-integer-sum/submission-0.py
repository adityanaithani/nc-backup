class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return ALL triplets with distinct i,j,k that sum to 0 
        # goal: i + j + k = 0
        # rewrite: j + k = -i

        # same as 2 sum: sort, two pointers to look for -a

        ret = []
        ordered = sorted(nums)
        for i in range(len(ordered)):
            if i > 0 and ordered[i] == ordered[i-1]:
                continue
            j = i + 1
            k = len(ordered) - 1
            while j < k:
                current_sum = ordered[i] + ordered[j] + ordered[k]
                if current_sum > 0:
                    k -= 1
                elif current_sum < 0:
                    j += 1
                else: 
                    ret.append([ordered[i],ordered[j],ordered[k]])
                    j += 1
                    k -= 1
                    while j < k and ordered[j] == ordered[j-1]:
                        j += 1
        return ret
                    
