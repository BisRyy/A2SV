# Enter your code here. Read input from STDIN. Print output to STDOUT

def piling(lst):
    i, j = 0, len(lst) - 1
    while i <= j:
        large = None
        
        if lst[j] > lst[i]:
            large = lst[j]
            j -= 1
            
        else :
           large = lst[i]
           i += 1  
           
        if i > j:
            return "Yes"
        
        if lst[j] > large or lst[i] > large :
            return "No"

for i in range(int(input())):
    no_of_cubes = int(input())
    cubes_list = list(map(int,input().split()))
    print(piling(cubes_list))
