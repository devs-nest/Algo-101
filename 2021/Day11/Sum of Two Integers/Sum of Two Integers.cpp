class Solution
{
public:
    int getSum(int a, int b)
    {
        if (b == 0)
            return a;
        int sum = a ^ b;                        // finding the sum
        int carry = (unsigned int)(a & b) << 1; // finding the carry
        return getSum(sum, carry);
    }
};