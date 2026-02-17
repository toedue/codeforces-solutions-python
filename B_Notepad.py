test_case = int(input())

for _ in range (test_case):
    n = int(input())
    s = input()

    d = {}
    
    for i in range(n-1):
        sub_string = s[i:i+2]

        if sub_string in d:
            prev_index = d[sub_string]
            # the previous substring must not overlap with the new substring
            if prev_index < i: 
                print("YES")
                break

        else:
            d[sub_string] = i + 1 #storing the last index
    else:
        print("NO")



    

