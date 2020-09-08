class FenwickTree:
    def __init__(self, n: int) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x) -> None:
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def __sum__(self, r: int):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def sum(self, l: int, r: int):
        assert 0 <= l <= r <= self._n
        return self.__sum__(r) - self.__sum__(l)
