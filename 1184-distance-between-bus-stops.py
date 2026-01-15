class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        
        c = sum(distance[start:destination])
        total = sum(distance)

        return min(c, total-c)
