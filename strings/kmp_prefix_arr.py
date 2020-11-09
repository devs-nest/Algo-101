# Hello World program in Python
    
print "Hello World!\n"


s = "acacabacacabacacac"
i = 1
j = 0
p_arr = [0]*len(s)

while(i<len(s)):
    if s[i] != s[j]:
        if j!=0 :
            j = j-1 
            j = p_arr[j] 
        elif j == 0:
            p_arr[i] = j
            i = i + 1

    elif s[i] == s[j]:
        j = j+1
        p_arr[i] = j
        i = i+1

print p_arr
"acacabacacabacacabacacabacacabacacac"


"acacabacacabacacac"
[0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 4]

          j                                   i
# [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17]
# ["a c a c a b a c a c  a  b  a  c  a  c  a  c"]
# [ 0 0 1 2 3 0 1 2 3 4  5  6  7  8  9  10 11  4                  ]




