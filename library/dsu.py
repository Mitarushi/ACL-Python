class DSU:
    def __init__(self, n):
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        stack = []
        while self.parent_or_size[a] >= 0:
            stack.append(a)
            a = self.parent_or_size[a]
        for i in stack:
            self.parent_or_size[i] = a
        return a

    def size(self, a):
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [self.leader(i) for i in range(self._n)]
        group_size = [0] * self._n
        for i in leader_buf:
            group_size[i] += 1
        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)
        result = [i for i in result if i]
        return result
