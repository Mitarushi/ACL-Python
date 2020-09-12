# https://atcoder.jp/contests/practice2/tasks/practice2_j

from library.segtree import SegTree

n, q = map(int, input().split())
a = list(map(int, input().split()))
seg = SegTree(a, max, lambda: -1)

for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        seg.set(x - 1, y)
    elif t == 2:
        print(seg.prod(x - 1, y))
    else:
        print(seg.max_right(x - 1, lambda v: v < y) + 1)
