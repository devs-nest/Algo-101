class Solution //By CyFun
{
public:
    int maxArea(vector<int> &height)
    {
        int lidx = 0, ridx = height.size() - 1, answer = 0;

        while (lidx < ridx)
        {
            int h = min(height[ridx], height[lidx]);
            int square = (ridx - lidx) * h;
            if (answer < square)
                answer = square;

            if (height[ridx] > height[lidx])
                lidx++;
            else
                ridx--;
        }

        return answer;
    }
};