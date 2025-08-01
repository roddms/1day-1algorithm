import sys
input = sys.stdin.readline
from queue import PriorityQueue

N, M, K, X = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append([b, 1])

INF = int(1e12)
dist = [INF] * (N+1)

pq = PriorityQueue()
pq.put([0,X])
dist[X] = 0

while not pq.empty():

    cur_dist, cur_city = pq.get()

    if cur_dist > dist[cur_city]:
        continue

    for adj_node, adj_dist in adj_lst[cur_city]:
        tmp_dist = adj_dist + cur_dist
        if tmp_dist < dist[adj_node]:
            dist[adj_node] = tmp_dist
            pq.put([tmp_dist, adj_node])

ans = []

for i in range(len(dist)):
    if dist[i] == K:
        ans.append(i)

if ans:
    for a in ans:
        print(a)

else:
    print(-1)