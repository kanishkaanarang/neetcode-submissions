class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed
        cars = list(zip(position, speed))

        # Sort cars by position in descending order (closest to target first)
        cars.sort(reverse=True)

        fleets = 0
        prev_time = 0

        for pos, spd in cars:
            # Time needed for this car to reach the target
            time = (target - pos) / spd

            # If this car takes longer than the fleet ahead,
            # it cannot catch up and forms a new fleet
            if time > prev_time:
                fleets += 1
                prev_time = time

        return fleets