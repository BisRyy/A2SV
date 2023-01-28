n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
if k==0 and a[0] > 1:
    print(a[0]-1)
elif k==n:
    print(a[n-1])
elif a[k-1] < a[k]:
    print(a[k-1])
elif a[k-1] == a[k]:
    print(-1)
elif a[k-1]+1 < a[k]:
    print(a[k-1]+1)
else:
    print(-1)
