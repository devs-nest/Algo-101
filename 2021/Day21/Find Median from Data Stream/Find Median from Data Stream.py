"""
        ## RC ##
        ## APPROACH : 2 HEAPS ##
        ## LOGIC ##
        ## One minheap to store low values and second maxheap to store max values, we keep track and update median every time after insertion ##
        
		## TIME COMPLEXITY : O(logN) ##
		## SPACE COMPLEXITY : O(N) ##

        ## EXAMPLE ##
        Adding number 41
        MaxHeap lo: [41]           // MaxHeap stores the largest value at the top (index 0)
        MinHeap hi: []             // MinHeap stores the smallest value at the top (index 0)
        Median is 41
        =======================
        Adding number 35
        MaxHeap lo: [35]          // max heap stores smaller half of nums
        MinHeap hi: [41]          // min heap stores bigger half of nums
        Median is 38
        =======================
        Adding number 62
        MaxHeap lo: [41, 35]
        MinHeap hi: [62]
        Median is 41
        =======================
        Adding number 4
        MaxHeap lo: [35, 4]
        MinHeap hi: [41, 62]
        Median is 38
        =======================
        Adding number 97
        MaxHeap lo: [41, 35, 4]
        MinHeap hi: [62, 97]
        Median is 41
        =======================
        Adding number 108
        MaxHeap lo: [41, 35, 4]
        MinHeap hi: [62, 97, 108]
        Median is 51.5
"""


class MedianFinder:
    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num):
        heappush(self.lo, -num)             # lo is maxheap, so -1 * num
        heappush(self.hi, -self.lo[0])      # hi is minheap
        heappop(self.lo)

        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (self.hi[0] - self.lo[0]) / 2  # - as low has -ve values
