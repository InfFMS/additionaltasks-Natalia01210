n = int(input())
a = n ** 0.5 // 1
for i in range(int(a), 0, -1):
    if(n % (i * i) == 0):
        print(i * i)
        break