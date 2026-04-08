import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if self.max_heap and num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if  self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            x, y = -heapq.heappop(self.max_heap), heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -y), heapq.heappush(self.min_heap, x)

        if len(self.min_heap) > len(self.max_heap):
            top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -top)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            top = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, top)
        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2


        # with python 3.14 we can use heapq.heappush/pop_max()
    # def __init__(self):
    #     self.small = []
    #     self.large = []

    # def addNum(self, num: int) -> None:
    #     heapq.heappush(self.large, heapq.heappushpop_max(self.small, num))
    #     if len(self.large) > len(self.small):
    #         heapq.heappush_max(self.small, heapq.heappop(self.large))

    # def findMedian(self) -> float:
    #     if len(self.small) > len(self.large):
    #         return self.small[0]
    #     return (self.small[0] + self.large[0]) / 2

        
        