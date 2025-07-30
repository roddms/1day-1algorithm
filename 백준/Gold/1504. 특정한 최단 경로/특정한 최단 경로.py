import sys
input = lambda: sys.stdin.readline().rstrip()

from queue import PriorityQueue

N, E = map(int, input().split())

adj_lst = [[] for _ in range(N+1)]

INF = int(1e12)

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_lst[a].append([b,c])
    adj_lst[b].append([a,c])

v1, v2 = map(int, input().split())

def dijkstra(start_node):
    global N, adj_lst

    dist = [INF] * (N+1)

    pq = PriorityQueue()
    pq.put([0,start_node])
    dist[start_node] = 0

    while not pq.empty():
        cur_dist, cur_node = pq.get()

        if cur_dist > dist[cur_node]:
            continue

        for adj_node, adj_dist in adj_lst[cur_node]:
            tmp_dist = cur_dist + adj_dist

            if tmp_dist < dist[adj_node]:
                pq.put([tmp_dist, adj_node])
                dist[adj_node] = tmp_dist

    return dist


dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

# 1 -> v1 -> v2 -> N
# 1 -> v2 -> v1 -> N
case1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
case2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]
best = min(case1, case2)

print(best if best < INF else -1)