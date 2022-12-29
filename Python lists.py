if __name__ == '__main__':
    N = int(input())
    ans = []
    for i in range(N):
        inp = input().split(' ')
        if inp[0] == 'insert':
            ans.insert(int(inp[1]), int(inp[2]))
        elif inp[0] == 'print':
            print(ans)
        elif inp[0] == 'append':
            ans.append(int(inp[1]))
        elif inp[0] == 'remove':
            ans.remove(int(inp[1]))
        elif inp[0] == 'pop':
            ans.pop()
        elif inp[0] == 'sort':
            ans.sort()
        else:
            ans.reverse()
