class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visitedCity = set()
        count = 0

        for i in range(len(isConnected)):
            if i not in visitedCity:
                stack = [i]
                while stack:
                    city = stack.pop()
                    if city not in visitedCity:
                        visitedCity.add(city)
                        for j in range(len(isConnected)):
                            if isConnected[city][j] == 1 and j not in visitedCity:
                                stack.append(j)
                count += 1
        return count
