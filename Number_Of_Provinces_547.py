class Solution(object):
    flag = []
    # Deepth first search
    def checkNode(self, isConnected, nodeNo):
        global flag
        i = 0
        while i < len(isConnected[nodeNo]):
            if isConnected[nodeNo][i] == 1 and flag[i] == 0:
                flag[i] = 1
                self.checkNode(isConnected, i)
                print(isConnected[nodeNo][i])
            i += 1

        return 1

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        global flag
        flag = [0] * len(isConnected)
        region = 0

        for nodeNo, node in enumerate(isConnected):
            if flag[nodeNo] == 0:
                flag[nodeNo] = 1
                region += 1
                self.checkNode(isConnected, nodeNo)
        print(region)
        return region


