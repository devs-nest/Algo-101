class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        double med = 0.0;
        for (int val : nums2)
        {
            nums1.push_back(val);
        }
        sort(nums1.begin(), nums1.end());
        int n = nums1.size();
        med = (n % 2 == 0) ? (double)(nums1[n / 2] + nums1[(n / 2) - 1]) / 2 : nums1[n / 2];

        return med;
    }
};