t = int(input())  
for i in range(t): 
    test = input() 
    len_test = len(test) 
    mid = len_test//2    
    if len_test % 2 == 0:   
        test1= test[:mid] 
        test2 = test[mid:] 
        if test1==test2:   
            print("YES")
        else:
            print("NO")  
    else:
        print("NO")