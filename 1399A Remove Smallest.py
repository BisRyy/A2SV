# import sys
# input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

for t in range(int(input())):
    n = int(input())
    arr = inlt()
    
    arr.sort()
    f = True
    for i in range(n-1):
        if not arr[i+1] - arr[i] <= 1:
            f = False
    if f:
        print("YES")
    else:
        print("NO")
