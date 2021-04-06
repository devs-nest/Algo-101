class Solution //By CyFun
{
public:
    bool isAnagram(string s, string t)
    {
        vector<int> temp(26, 0);
        if (s.length() != t.length())
            return false;
        for (int i = 0; i < s.length(); i++)
        {
            temp[(int)s[i] - (int)'a']++;
            temp[(int)t[i] - (int)'a']--;
        }
        for (int i = 0; i < 26; i++)
        {
            if (temp[i] != 0)
                return false;
        }
        return true;
    }
};