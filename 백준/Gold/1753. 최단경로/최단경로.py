import sys
input = sys.stdin.readline


from queue import PriorityQueue

V, E = map(int, input().split())

K = int(input())

INF = int(1e12)
dist = [INF] * (V+1)

adj_lst = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_lst[a].append([b, c])

#print(adj_lst)
    
pq = PriorityQueue()
pq.put([0, K])
dist[K] = 0

while not pq.empty():
    cur_dist, cur_node = pq.get()

    if cur_dist > dist[cur_node]: # 현재 경로가 기존 경로보다 길다면 의미 없으므로 pass
        continue

    for adj_node, adj_dist in adj_lst[cur_node]:
        tmp_dist = cur_dist + adj_dist

        if tmp_dist < dist[adj_node]:
            pq.put([tmp_dist, adj_node])
            dist[adj_node] = tmp_dist


for i in range(1,V+1):
    if dist[i] == INF:
        print('INF')

    else: 
        print(dist[i])