n, m, k = int(input()), int(input()), int(input())
if k % n == 0 and n <= k and n * m >= k: print("YES")
elif k % m == 0 and m <= k and n * m >= k: print("YES")
else: print("NO")