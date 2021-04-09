class Solution
{
public:
    long long binarySearch(int x)
    {
        long long s = 2, e = x / 2 + 1, mid;
        while (s <= e)
        {
            mid = s + (e - s) / 2;
            if (mid * mid == x || mid * mid < x && (mid + 1) * (mid + 1) > x)
                break;
            else if (mid * mid > x)
                e = mid - 1;
            else
                s = mid + 1;
        }
        return mid;
    }

    int mySqrt(int x)
    {
        if (x == 0)
            return 0;
        if (x < 4)
            return 1;
        return binarySearch(x);
    }
};