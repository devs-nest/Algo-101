class Solution
{
public:
    bool isValid(string s)
    {
        std::unordered_map<char, char> match{{')', '('}, {']', '['}, {'}', '{'}};
        std::deque<char> stack;
        for (const auto &c : s)
        {
            if (c == '(' || c == '[' || c == '{')
                stack.push_back(c);
            else
            {
                if (stack.empty() || stack.back() != match[c])
                    return false;
                stack.pop_back();
            }
        }
        return (stack.empty());
    }
};