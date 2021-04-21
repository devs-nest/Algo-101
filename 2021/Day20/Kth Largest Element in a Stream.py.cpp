class KthLargest
{
public:
    priority_queue<int, vector<int>, greater<int>> pq;
    int size, gk;
    KthLargest(int k, vector<int> &nums)
    {
        int n = nums.size();
        gk = k;
        if (n < k)
            size = n;
        else
            size = k;
        for (int i = 0; i < size; i++)
            pq.push(nums[i]);
        for (int i = k; i < n; i++)
        {
            if (nums[i] > pq.top())
            {
                pq.pop();
                pq.push(nums[i]);
            }
        }
    }

    int add(int val)
    {
        if (pq.empty() || pq.size() < gk)
            pq.push(val);
        else if (val > pq.top())
        {
            pq.pop();
            pq.push(val);
        }
        return pq.top();
    }
};
/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */