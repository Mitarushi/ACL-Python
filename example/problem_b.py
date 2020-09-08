# https://atcoder.jp/contests/practice2/tasks/practice2_b

from library.fenwicktree import FenwickTree

n, q = map(int, input().split())

fw = FenwickTree(n)
for index, i in enumerate(map(int, input().split())):
    fw.add(index, i)

for _ in range(q):
    t, p, x = map(int, input().split())
    if t == 0:
        fw.add(p, x)
    else:
        print(fw.sum(p, x))
