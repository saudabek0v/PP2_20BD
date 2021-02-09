a = [int(i) for i in input().split()]
for i in range(len(a)):
    if a[i] == 0:
        for j in range(i + 1, len(a)):
            if a[j] != 0:
                a[i], a[j] = a[j], a[i]
                break
print(*a)