class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visitedRooms = set()
        stack = [0]

        while stack:
            room = stack.pop()
            if room not in visitedRooms:
                visitedRooms.add(room)
                for key in rooms[room]:
                    if key not in visitedRooms:
                        stack.append(key)
                
        return len(visitedRooms) == len(rooms)
        