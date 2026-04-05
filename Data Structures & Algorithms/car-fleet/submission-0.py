class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # OBJECTIVE: return number of different car fleets that will arrive at destination
        # O(nlogn) time and O(n) space

        # similar to other stack problems, only care about the car in front of you

        # 1. calculate time to target by (target-position) / speed
        # 2. sort cars by position - start from CLOSEST to target  
        # 3. if a car behind car x takes leq time to reach target than the car in front, it is part of the fleet

        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for p, s in pair:
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
        
