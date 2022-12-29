# Enter your code here. Read input from STDIN. Print output to STDOUT

values = set(map(int, input().split()))

ans = True
for tests in range(int(input())):
    next_set = set(map(int, input().split()))
    
    for item in next_set:
        if item not in values or len(next_set) > len(values):
            ans = False
            break
            
if ans:
    print("True")
else:
    print("False")
    
            
