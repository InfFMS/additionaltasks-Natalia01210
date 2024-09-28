s = input()
a = 0
x = 0
y = 0
for i in range(len(s)):
    if(s[i] != 'W' and s[i] != 'N' and s[i] != 'S' and s[i] != 'E'):
        a = a * 10 + int(s[i])
    else:
        if(s[i] == 'W'):
            x -= a
            a = 0
        elif(s[i] == 'E'):
            x += a
            a = 0