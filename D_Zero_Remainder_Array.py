t = int(input())
for i in range (t):
    n, k = map(int,(input().split()))
    arr = list(map(int, (input().split())))

    freq = {}

    # calculate needed values
    for num in arr:
        r = num % k
        if r != 0:
            need = k - r
            if need in freq:
                freq[need] += 1
            else:
                freq[need] = 1
    
    # if everything already divisible
    if len(freq) == 0:
        print(0)
        continue


    # find maximum time

    answer = 0 # this will store the biggest finishing time

    for need in freq:
        frequency = freq[need]
        last_time = need + (frequency-1) * k

        if last_time > answer:
            answer = last_time

    #we add 1 because operations start from time 0    
    print(answer + 1)

    



