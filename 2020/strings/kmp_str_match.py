str = "abxabcabcaby" #n
p = "abcaby" # m
p_arr = [0, 0, 0, 1, 2, 0]

i = 0
j = 0
f = True

while(i<len(str)):
    if str[i] == p[j]:
        i += 1
        j += 1
    else:
        if j == 0:
            i += 1
        else:
            j = p_arr[j-1]
        
    if j == len(p):
        print True
        f = False
        break
    
if f:   
    print False
