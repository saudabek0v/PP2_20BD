m, n = map(int, input().split())
a_m, b_n, res = [], [], []
for i in range(m): a_m.append(int(input()))
for i in range(n): b_n.append(int(input()))
s = set.intersection(set(a_m), set(b_n))
for i in s: res.append(i)
res.sort()
cnt_a, cnt_b = 0, 0
a_x, b_x = [], []
for i in a_m:
    if i not in res:
        cnt_a += 1
        a_x.append(i)
for i in b_n:
    if i not in res:
        cnt_b += 1
        b_x.append(i)
a_x.sort()
b_x.sort()
print(len(res))
print(*res)
print(cnt_a)
print(*a_x)
print(cnt_b)
print(*b_x)