#
#
# Merging intervals
#
#
# #Given a list of intervals [x,y] remove all the intervals [a,b] for which there exists  an interval
# #[c,d] where c<=a,b<=d ==
#
#
# 6
#
# 1 2
# 3 6
# 4 5
# 7 10
# 8 9
# 8 10
#
# 1<=N<10^5
#
# n square will not work
# n logN OR N
#
# # # # # # # # # # #
# 1 2 3 4 5 6 7 8 9 10
#
#
# 1 2
# 3 6
# 7 10
#
# O(N*N)
# for set in allSets:  N
#     for superSet in allSet: N-1
#         if set lies in superSet:
#             remove it
#
#
# let's sort the array of intervals first in increasing order of second element and then sort it
# on the basis of first
#
# O(NlogN)
# 1 2
# 3 6
# 4 5
# 7 10
# 8 9
# 8 10
#
# Sort it,
# 1. on the basis of second element,
# 1 2
# 4 5
# 3 6
# 8 9
# 7 10
# 8 10,
#
# 2. On the basis of first element
# 1 2 , i = 0
# 3 6 j=1
# 4 5
# 7 10 j =2
# 8 9
# 8 10
#
# j = 1
#
# for set in allSets:
#     j++
#     while j < n && set[j] lies in set[i]:
#         delete set[j]
#         j++
#
#
#         1,2
#             ->
#         [3,6]
#             ->
#                 [4,5]
#         [7,10]
#             ->
#                 [8,9] , [8,10]
#
#
#
#
