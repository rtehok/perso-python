from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited = [False] * len(rooms)
        # queue = collections.deque([(0, rooms[0])])
        #
        # while queue:
        #     room_number, current_room_keys = queue.popleft()
        #
        #     if not visited[room_number]:
        #         visited[room_number] = True
        #         for key in current_room_keys:
        #             queue.append((key, rooms[key]))
        #
        # return all(visited)
        visited = [False] * len(rooms)
        visited[0] = True
        stack = [0]

        while stack:
            curr_room = stack.pop()

            for key in rooms[curr_room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)

        return all(visited)


if __name__ == "__main__":
    assert Solution().canVisitAllRooms([[1], [2], [3], []])
    assert not Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
