# https://atcoder.jp/contests/practice2/tasks/practice2_a

from library.dsu import DSU

n, q = map(int, input().split())
dsu = DSU(n)

for _ in range(q):
    t, u, v = map(int, input().split())
    if t == 0:
        dsu.merge(u, v)
    else:
        print(1 if dsu.same(u, v) else 0)
