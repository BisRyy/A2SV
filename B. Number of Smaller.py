m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

j = 0
for i in range(n):
    while j < m and a[j] < b[i]:
        j+=1
    b[i] = j

print(*b)
# 1 2 3 6 8 9 13 13 15 18 18 21 25 
