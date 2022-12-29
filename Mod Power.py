# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
m = int(input())

def power(a, b):
    return pow(a,b)

def powermod(c, m):
    return c % m

c = power(a , b)
print(c)
print(powermod(c,m))
