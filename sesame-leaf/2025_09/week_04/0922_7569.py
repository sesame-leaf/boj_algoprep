import sys
from collections import deque


class Bfs:
    def __init__(
            self, 
            map: list[list[list[int]]], 
            start_vertex: list[tuple[int, int, int]]
    ):
        self.__map: list[list[list[int]]] = map
        self.__start_vertex: list[tuple[int, int, int]] = start_vertex
        self.__stacks: int = len(map)
        self.__height: int = len(map[0])
        self.__width: int = len(map[0][0])
        self.__queue: deque[tuple[int, int, int]] = deque(self.__start_vertex)
        self.__cycle_counter: int = 0
        self.__dx = (1, 0, 0, -1, 0, 0)
        self.__dy = (0, 1, 0, 0, -1, 0)
        self.__dz = (0, 0, 1, 0, 0, -1)
    
    def __call__(self) -> int:
        while self.__queue:
            self.__bfs_one_cycle()
            self.__cycle_counter += 1
        
        return self.__cycle_counter

    def __bfs_one_cycle(self) -> None:
        queue_len: int = len(self.__queue)
        for _ in range(queue_len):
            x, y, z = self.__queue.popleft()
            for i in range(6):
                neighbor: tuple[int, int, int] = (x+self.__dx[i], y+self.__dy[i], z+self.__dz[i])
                if self.__can_go(neighbor):
                    self.__map[neighbor[2]][neighbor[1]][neighbor[0]] = 1
                    self.__queue.append(neighbor)
    
    def __can_go(self, vertex: tuple[int, int, int]) -> bool:
        x, y, z = vertex
        return ((0 <= x) and (x < self.__width)) and ((0 <= y) and (y < self.__height)) and ((0 <= z) and (z < self.__stacks)) and (self.__map[z][y][x] == 0)


def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    # Get data
    M, N, H = map(int, input().split())
    tomato_box_stack: list[list[list[int]]] = list() # tomato_box[z][y][x]
    riped_tomatos: list[tuple[int, int, int]] = list()
    for i in range(H):

        tomato_box: list[list[int]] = list()
        for j in range(N):
            row = list(map(int, input().split()))
            tomato_box.append(row)

            for k in range(M):
                # Find riped tomatos
                if row[k] == 1:
                    riped_tomatos.append((k, j, i))

        tomato_box_stack.append(tomato_box)
    
    min_ripe_days = Bfs(tomato_box_stack, riped_tomatos)() - 1

    all_tomato_riped: bool = True
    for box in tomato_box_stack:
        for row in box:
            for tomato in row:
                if tomato == 0:
                    all_tomato_riped = False
                    break
            if tomato == 0:
                break
        if tomato == 0:
            break
    
    if all_tomato_riped:
        print(min_ripe_days)
    else:
        print(-1)
    

if __name__ == "__main__":
    main()
