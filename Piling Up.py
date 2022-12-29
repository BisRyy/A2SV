# Enter your code here. Read input from STDIN. Print output to STDOUT

def piling(d):
    i, j = 0, 0
    while d:
        large = None
        if d[-1-j] > d[0+i]:
            large = d[-1-j]
            j += 1
        else :
           large = d[0+i]
           i += 1
            
        if len(d) - i - j == 0 :
            return "Yes"
        
        if d[-1-j] > large or d[0+i] > large :
            return "No"

for i in range(int(input())):
    no_of_cubes = int(input())
    l = list(map(int,input().split()))
    print(piling(l))
