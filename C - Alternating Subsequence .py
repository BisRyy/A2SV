for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    
    f = 0 if a[0] > 0 else 1
    maximum = a[0]
    answer = 0
    for i in a:
        if f == 0 and i > 0:
            maximum = max(i, maximum)
        elif f == 0 and i < 1:
            f = 1
            answer += maximum
            maximum = i
        elif f == 1 and i > 0:
            f = 0
            answer += maximum
            maximum = i
        else:
            maximum = max(i, maximum)
    
    answer += maximum
    print(answer)
            
            
