class MedianFinder
{
private:
    int size;
    multiset<int> numsSet;
    multiset<int>::iterator midIter;

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        if (numsSet.empty())
        {
            midIter = numsSet.insert(num);
            size++;
            return;
        }
        numsSet.insert(num);
        if ((size & 1) && num < *midIter)
            --midIter;
        else if (!(size & 1) && num >= *midIter)
            ++midIter;
        size++;
    }

    // Returns the median of current data stream
    double findMedian()
    {
        if (size & 1)
            return *midIter;
        else
            return (double)(*midIter + *next(midIter)) / 2;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */