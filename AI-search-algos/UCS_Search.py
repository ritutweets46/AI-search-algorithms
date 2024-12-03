
import random
from collections import deque
import heapq

class Fringe:
    def __init__(self):
        self.priorityQ = []

    def insert(self, i, cost):
        heapq.heappush(self.priorityQ, (cost, i))

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

fringe = Fringe()
print()
print("-----Starting Search-----")
print()
start_state = [(0, N - 1)]

fringe.insert(start_state,0)
print(f"inserted node is, {mat[0][N - 1]}")
closed_set = set()

solved = False

while (True):
    cost, pt = fringe.delete()
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
        children.append((pt + [(ci, cj - 1)], cost + 1))  # Cost + 1 for left move
    if (cj + 1 <= N - 1) and (ci, cj + 1) not in closed_set:  # right move
        children.append((pt + [(ci, cj + 1)], cost + 1))  # Cost + 1 for right move
    if (ci - 1 >= 0) and (ci - 1, cj) not in closed_set:  # up move
        children.append((pt + [(ci - 1, cj)], cost + 2))  # Cost + 2 for up move
    if (ci + 1 <= N - 1) and (ci + 1, cj) not in closed_set:  # down move
        children.append((pt + [(ci + 1, cj)], cost + 2))  # Cost + 2 for down move


    # Insert all children into the fringe
    for child, child_cost in children:
        fringe.insert(child, child_cost)
        print(f"inserted node is, {mat[child[-1][0]][child[-1][1]]}, cost: {child_cost}")

    print("Visited Nodes:  ", closed_set)

if (solved):
    print()
    print("Search successful. Found at ", (ci, cj))
    print()
    print("Path Solution:", pt)
else:
    print("Search Failed")