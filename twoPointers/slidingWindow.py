# Given an array of size N, we need to find the maximum sum of consecutive K elements
# [1,2,3,100,200,300,400,200,500]
# k = 3
# for i in [1,2,3,100,200,300,400,200,500]:
#   tempSum = 0
#   for j in (i,i+k):
#       tempSum = tempSum+a[i]
#  ans = max(ans, tempSum)


#Time complexity - O(n*n)
# [1,2,3,100,200,300,400,200,500]
# 6, x = [1,2,3]
# 6 + 100 -1 [2,3,100], x+100-1
# (6 + 100 -1) + 200 -2

if __name__ == '__main__':
    k = 3
    l = raw_input().split(' ');
    my_list = list(int(num) for num in l)
    maxSum = 0
    i = 0
    j = 0
    n = len(my_list)
    maxSum = 0
    while j < k:
        maxSum = maxSum + my_list[j]
        j = j +1
    print maxSum
    tempSum = maxSum
    while j < n:
        j = j + 1
        tempSum = tempSum + my_list[j] - my_list[i]
        i = i +1
        maxSum = max(maxSum, tempSum)
    print maxSum



