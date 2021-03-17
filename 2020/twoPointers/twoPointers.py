#Given a sorted array, we need to find a pair of numbers a[i] and a[j] whose sum is K
# a = [1,2,3,4,5,10]
# i -> [1,2,3,4,5,10]:
#   j->i+1....[1,3,4,5,6,10]:
#       if a[i] + a[j] == k:
#           print a[i]
#           print a[j]
#Time complexity -  O(n*n)


# i = 0
# j = n-1

# while i<j:
#  if a[i] + a[j] == k:
#    print a[i] and print a[j]
#  if a[i]+ a[j]> k:
#         j--
#     else:
#         i++

#Time complexity- O(n)

if __name__ == '__main__':
    k =9
    l = raw_input().split(' ');
    my_list = list(int(num) for num in l)
    print my_list
    i = 0
    j = len(my_list) -1
    while i<j:
     if my_list[i] + my_list[j] == k:
       print my_list[i]
       print my_list[j]
     if my_list[i]+ my_list[j]> k:
            j = j - 1
     else:
         i = i + 1

