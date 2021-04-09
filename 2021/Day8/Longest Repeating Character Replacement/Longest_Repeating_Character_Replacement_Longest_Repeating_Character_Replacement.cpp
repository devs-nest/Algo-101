class Solution
{
public:
    int characterReplacement(string s, int k)
    {
        int size = s.size(), i = 0, j = 0, same = 0;
        vector<int> m(128, 0);
        while (j < size)
        {
            same = max(same, ++m[s[j++]]); // Update table, count for maximum character in window, and increment right bound
            if (j - i - same > k)
                --m[s[i++]]; // If criteria is not satisfied, increment left bound, update table
        }
        return j - i;
    }
};
