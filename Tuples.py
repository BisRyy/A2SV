if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    m = [int(i) for i in integer_list]
    t = tuple(m)

    v = hash(t)
    print(v)
