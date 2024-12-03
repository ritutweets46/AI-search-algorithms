import random
from collections import deque
import heapq

class Fringe:
    def __init__(self):
        self.priorityQ = []

    def insert(self, i, h_value):
        heapq.heappush(self.priorityQ, (h_value, i))

    def delete(self):
        if self.priorityQ:
            return heapq.heappop(self.priorityQ)
        else:
            return -1


def goal_test(mat, i, j, e):
    if (mat[i][j] == e):
        return True
    else:
        return False

def heuristic_value(x, y, ei, ej):
    #dist b/w A(x1,y1) and G(x2,y2) is |x1-x2|+|y1-y2|
    # A(x,y) and G(ei,ej) is |x-ei|+|y-ej|
    manhattan_dist = abs(x-ei) + abs(y-ej)
    return manhattan_dist

print("Setting up the problem")

print("Insert N")
N = int(input())

data = random.sample(range(1, 1000), N * N)

mat = []
for ii in range(N):
    loc = []
    for jj in range(N):
        loc.append(data[ii * N + jj])

    mat.append(loc)

print()
print("-----Matrix for Search-----")
print()
print("S denotes start state")
print()
for ii in range(N):
    rowstr = ""
    for jj in range(N):
        if (ii == 0 and jj == N - 1):
            rowstr += " " + str(mat[ii][jj]) + "(S) "
        else:
            rowstr += " " + str(mat[ii][jj]) + " "
    print(rowstr)

print()
print("Insert target number e between 1 and 999")
e = int(input())

for ii in range(N):
    for jj in range(N):
        if(e == mat[ii][jj]):
            ei = ii
            ej = jj
            break


fringe = Fringe()
print()
print("-----Starting Search-----")
print()
start_state = [(0, N - 1)]

fringe.insert(start_state,heuristic_value(0,N-1, ei, ej))
print(f"inserted node is, {mat[0][N - 1]}")
closed_set = set()

solved = False

while (True):
    h_value, pt = fringe.delete()
    if (pt == -1):
        break
    if (pt[-1] in closed_set):
        continue
    closed_set.add(pt[-1])

    (ci, cj) = pt[-1]

    if (goal_test(mat, ci, cj, e)):
        solved = True
        break

    children = []
    if (cj - 1 >= 0) and (ci, cj - 1) not in closed_set:  # left move
        children.append((pt + [(ci, cj - 1)], heuristic_value(ci, cj - 1, ei, ej)))  # left move
    if (cj + 1 <= N - 1) and (ci, cj + 1) not in closed_set:  # right move
        children.append((pt + [(ci, cj + 1)], heuristic_value(ci, cj + 1, ei, ej)))  # right move
    if (ci - 1 >= 0) and (ci - 1, cj) not in closed_set:  # up move
        children.append((pt + [(ci - 1, cj)], heuristic_value(ci - 1, cj, ei, ej)))  # up move
    if (ci + 1 <= N - 1) and (ci + 1, cj) not in closed_set:  # down move
        children.append((pt + [(ci + 1, cj)], heuristic_value(ci + 1, cj, ei, ej)))  # down move


    # Insert all children into the fringe
    for child, h_value in children:
        fringe.insert(child, h_value)
        print(f"inserted node is, {mat[child[-1][0]][child[-1][1]]}, heuristic value: {h_value}")

    print("Visited Nodes:  ", closed_set)

if (solved):
    print()
    print("Search successful. Found at ", (ci, cj))
    print()
    print("Path Solution:", pt)
else:
    print("Search Failed")