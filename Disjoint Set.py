# UnionFind class
class QuickFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def findRoot(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.findRoot(x) == self.findRoot(y)


class QuickUnion:

    def __init__(self, size):
        self.root = [i for i in range(size)]

    def findRoot(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)

        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.findRoot(x) == self.findRoot(y)


class UnionByRank:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def findRoot(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.findRoot(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.findRoot(x) == self.findRoot(y)


# Path compression optimizations UNION FIND.

class PcoUnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def findRoot(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.findRoot(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)
        if rootX != rootY:
            self.root[rootY] = self.root[rootX]

    def connected(self, x, y):
        return self.findRoot(x) == self.findRoot(y)


if __name__ == "__main__":
    # Test Case
    uf = UnionByRank(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true
