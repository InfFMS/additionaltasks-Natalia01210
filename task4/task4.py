n = int(input())
if(n % 2 == 1 and (n - 1) % 4 == 0) or (n % 2 == 0 and n % 4 != 0):
    print("IMPOSSIBLE")
else:
    if(n % 2 == 0):
        a = 0;
        for i in range(1, int(n/2) + 1):
            if(a == 0):
                print('-', end='')
                a += 1
                a %= 2
            else:
                print('+', end='')
                a += 1
                a %= 2
        a += 1
        a %= 2
        for i in range(int(n/2) + 1, n+1):
            if (a == 0):
                print('-', end='')
                a += 1
                a %= 2
            else:
                print('+', end='')
                a += 1
                a %= 2
    else:
        a = 0;
        for i in range(1, int(n // 2) + 1):
            if (a == 0):
                print('-', end='')
                a += 1
                a %= 2
            else:
                print('+', end='')
                a += 1
                a %= 2
        a += 1
        a %= 2
        for i in range(int(n // 2) + 1, n + 1):
            if (a == 0):
                print('-', end='')
                a += 1
                a %= 2
            else:
                print('+', end='')
                a += 1
                a %= 2