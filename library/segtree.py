from typing import Callable, TypeVar, List

T = TypeVar('T')


class SegTree:
    def __init__(self, v: List[T], op: Callable[[T, T], T], e: Callable[[], T]) -> None:
        self._n = len(v)
        self.log = (self._n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e() for _ in range(2 * self.size)]
        self.op = op
        self.e = e
        for i in range(self._n):
            self.d[self.size + i] = v[i]
        for i in reversed(range(1, self.size)):
            self.__update__(i)

    @classmethod
    def init_e(cls, n: int, op: Callable[[T, T], T], e: Callable[[], T]) -> 'SegTree':
        return cls([e() for _ in range(n)], op, e)

    def set(self, p: int, x: T) -> None:
        assert 0 <= p < self._n
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.__update__(p >> i)

    def get(self, p: int) -> T:
        assert 0 <= p < self._n
        return self.d[p + self.size]

    def prod(self, l: int, r: int) -> T:
        assert 0 <= l <= self._n and 0 <= r <= self._n
        sml = self.e()
        smr = self.e()
        l += self.size
        r += self.size

        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self) -> T:
        return self.d[1]

    def max_right(self, l: int, f: Callable[[T], bool]):
        assert 0 <= l <= self._n
        assert f(self.e())
        if l == self._n:
            return self._n
        l += self.size
        sm = self.e()
        while True:
            while l % 2 == 0:
                l >>= 1
            if not f(self.op(sm, self.d[l])):
                while l < self.size:
                    l *= 2
                    if f(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                return self._n

    def min_left(self, r: int, f: Callable[[T], bool]):
        assert 0 <= r <= self._n
        assert f(self.e())
        if r == 0:
            return 0
        r += self.size
        sm = self.e()
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not f(self.op(self.d[r], sm)):
                while r < self.size:
                    r = 2 * r + 1
                    if f(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r:
                return 0

    def __update__(self, k: int) -> None:
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])
