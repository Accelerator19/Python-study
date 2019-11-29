n = int(input())
li = [0,1]
for i in range(n-2):
    li.append(li[-2]+li[-1])
for i in li:
    print(i)
