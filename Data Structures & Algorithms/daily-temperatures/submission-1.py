class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return number of days after ith day before its warmer
        # on time and space

        # iterate thru, similar to min stack problem but max - if found new max update max stack, return max stack

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            current = temperatures[i]

            while stack and current > temperatures[stack[-1]]:
                popped = stack.pop()
                res[popped] = i - popped
            
            stack.append(i)

        return res