num=int(input())

words={}
for i in range(num):
    word=input()
    if word in words:
        words[word]=words[word] + 1
    else:
        words[word]=1
        
print(len(words))
print(*words.values())
