

Given a string t with length N and string s with length M find number of occurences
of string t in string S


ex:


3
for i in string t:
    substring temp = t[i]....t[i+M]
    for j in string s
        if s ===

O(N*m)

KMP
#. Prefix of a string

abcbdabdab
0 1 2 3 4 5 6 7
a b c d a b c d
[0, 0, 0, 0, 1, 2, 3 , 4]

0 1 2 3 4 5 6
a a b a a a b
[0, 1, 0, 1, 2, 2, 3]

0 1 2 3 4 5 6 7 8
a b c a b c a b c

[0, 0, 0, 1, 2, 3, 4 ,5 , 6]

prefix_function[5] = 2

a b c a b c a
03
abca
36
abca
0 1 2 3 4
a a a a a
[0,1,2,3,4]


pattern - s
text - t
temp s + '#' + t
calculate prefix
s - ab
t - abcbdabdab

ab+ '#' + abcbdabdab
prefix function 2

string temp = s + # + t

1. create a temporary pattern
3. Calculate prefix function
4. calculate occurence of string in result prefix function.


Prefix function - O(N+M) = O(n)
O(n)

O(N)

pattern = divya
text = divyanshu
divya#divyanshud
count = 0
prefix = [0, 0 , 0 , 0 ,0, 0, 1, 2, 3, 4, 5, 0,0,0, 0, 1 ]
for i in range(0, prefix):
    if prefix[i] == len(pattern):
        count = count + 1
print count

     0  1  2  3 4   5
s = [a, b, c, a,b, c]
[0, 0, 0, 1, 2, 3]

 i  = 4
 j = 1

def calculatePrefixFunction(s):
    pi = []
    n = len(s)
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = p[j-1]
        if s[i]==s[j]:
            j = j +1
        pi[i] = j
    return pi

[0, ]




