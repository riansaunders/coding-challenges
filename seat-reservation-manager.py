import heapq


class SeatManager:
    def __init__(self, capacity):
        self.seats = [ (x + 1) for x in range(capacity) ]
    
    def reserve(self):
        return heapq.heappop(self.seats)

    def unreserve(self, seat):
        return heapq.heappush(seat)

sm = SeatManager(5)


print(sm.reserve())