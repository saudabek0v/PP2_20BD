a, k = [int(i) for i in input().split()], int(input())
def rotate(a, k):
    return a[-k:] + a[:-k]
print(*rotate(a, k))