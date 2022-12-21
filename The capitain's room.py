families = int(input()) + 1
rooms = input().split(" ")
count = {}
for room in rooms:
    if room in count:
        count[room] = count[room] + 1
    else:
        count[room] = 1


for k in count.keys():
    if count[k] == 1:
        print(k)
        break
