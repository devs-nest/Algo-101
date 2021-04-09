class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int n = s.size(), rez = 0;
        int frec[128] = {0};
        for (int pos = 0, i = 0; pos < n; pos++)
        {
            i = max(frec[s[pos]], i);
            rez = max(rez, pos - i + 1);
            frec[s[pos]] = pos + 1;
        }
        return rez;
    }
};