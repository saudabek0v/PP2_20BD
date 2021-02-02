n = int(input())
if n >= 0: print(int(((1 + n) * n) // 2))
else:
    n = abs(n)
    print(int(-((1 + n) * n) // 2) + 1)