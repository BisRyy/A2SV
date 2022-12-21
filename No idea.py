nums = input().split(" ")
vals = input().split(" ")
likes = set(input().split(" "))
dislikes = set(input().split(" "))

happiness = 0

for val in vals:
    if val in likes:
        happiness = happiness + 1
    if val in dislikes:
        happiness = happiness - 1

print(happiness)
