class Solution
{
public:
    void subsetsWithDup(const vector<int> &sp,    // sub problem
                        int spi,                  // sub problem index
                        vector<int> &ps,          // partial solution
                        int psi,                  // partial solution index
                        vector<vector<int>> &res) // result vector
    {
        // base case if sub problem index == sp.size that means
        // there are no more numbers to be considered for subset
        // This branch has hit the end and partial solution we have
        // is the complete solution
        if (spi == sp.size())
        {
            res.push_back({ps.begin(), ps.begin() + psi});
            return;
        }

        // We need to take care of duplicate numbers
        // since we have already sorted the nums
        // all the duplicates are placed next to each other.
        // This loop takes care of counting occurences of any number
        // in case of duplicate it counts all occurences of duplicates
        int count{1};
        for (int i = spi + 1; i < sp.size() && sp[i] == sp[spi]; i++)
            ++count;

        // if we count the number of occurence of the number
        // then we can avoid duplicates and easily guess the
        // end of each unique branch
        // This way we can even optimize the solution.
        // eg: 2, 2, 2 (3 consecutive 2's)
        // Then resultant subsets we can have is numbers in subset till this point
        // + {} exclude case, {2} include one instance, {2, 2} include two instances
        // {2, 2, 2} include all three instances

        // exclude case:
        // Skip count number of elements as exclude case will not have any
        // occurence of this element
        subsetsWithDup(sp, spi + count, ps, psi, res);

        // include case:
        // include incrementally one instance in one branch,
        // two instances.. upto count instances
        for (int i = 0; i < count; i++)
        {
            ps[psi + i] = sp[spi];
            subsetsWithDup(sp, spi + count, ps, psi + i + 1, res);
        }
    }

    vector<vector<int>> subsetsWithDup(vector<int> &nums)
    {
        vector<vector<int>> res;
        vector<int> slate(nums.size(), 0);
        std::sort(nums.begin(), nums.end());
        subsetsWithDup(nums, 0, slate, 0, res);
        return res;
    }
};