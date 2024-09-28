a, b, c = int(input()), int(input()), int(input())
print(a + b + c - max(max(a, b), c) - min(min(a, b), c))