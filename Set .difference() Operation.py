# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
a = set(input().split())

m = int(input())
b = set(input().split())

count = 0
for item in a:
    if item not in b:
        count += 1
print(count)
