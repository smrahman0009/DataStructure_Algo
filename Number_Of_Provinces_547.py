class Solution(object):
    # union find method
    def findParent(self, parent, node):
        if parent[node] == -1:
            return node
        return self.findParent(parent, parent[node])

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        parent = [-1] * len(isConnected)
        region = len(isConnected)
        node = 0
        while node < len(isConnected):
            path = 0
            while path < len(isConnected[node]):
                if isConnected[node][path] == 1 and node != path:
                    parentNode = self.findParent(parent, node)
                    parentPath = self.findParent(parent, path)
                    if parentNode != parentPath:
                        parent[parentNode] = parentPath
                        region -= 1
                path += 1
            node += 1
        print(parent)
        return region


