class Solution //CyFun
{
public:
    vector<int> spiralOrder(vector<vector<int>> &v)
    {
        int n = v.size();
        int m = v[0].size();
        vector<int> a;
        int minr = 0;
        int minc = 0;
        int maxr = n - 1;
        int maxc = m - 1;
        int c = 0;
        int tne = n * m;
        while (c < tne)
        {
            //up left
            for (int i = minr, j = minc; j <= maxc && c < tne; j++)
            {
                a.push_back(v[i][j]);
                c++;
            }
            minr++;

            //rightB
            for (int i = minr, j = maxc; i <= maxr && c < tne; i++)
            {
                a.push_back(v[i][j]);
                c++;
            }
            maxc--;
            //downleft
            for (int i = maxr, j = maxc; j >= minc && c < tne; j--)
            {
                a.push_back(v[i][j]);
                c++;
            }
            maxr--;
            //leftUp

            for (int i = maxr, j = minc; i >= minr && c < tne; i--)
            {
                a.push_back(v[i][j]);
                c++;
            }
            minc++;
        }
        return a;
    }
};