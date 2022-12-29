import textwrap

def wrap(string, max_width):
    ans = ""
    c = 0
    for i in string:
        ans += i
        c += 1
        if c == max_width:
            ans += "\n"
            c = 0
            continue
        
    return ans

if __name__ == '__main__':
