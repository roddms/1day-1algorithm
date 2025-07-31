from queue import PriorityQueue

N, M, X = map(int, input().split()) # 정점, 간선, 목적지
adj_lst = [[] for _ in range(N+1)]
INF = int(1e12)

# 그래프 만들기
for _ in range(M):
    a,b,c = map(int, input().split())
    adj_lst[a].append([b,c])

def dijkstra(snode):
    global N, adj_lst

    time = [INF] * (N+1)
    pq = PriorityQueue()
    pq.put([0, snode])
    time[snode] = 0

    while not pq.empty():
        cur_time, cur_node = pq.get()

        if cur_time > time[cur_node]:
            continue

        for adj_node, adj_time in adj_lst[cur_node]:
            tmp_time = cur_time + adj_time
            if tmp_time < time[adj_node]:
                pq.put([tmp_time, adj_node])
                time[adj_node] = tmp_time

    return time

time = [-9999] * (N+1)

for i in range(1, N+1):
    time[i] = dijkstra(i)

ans = -1
for i in range(1, N+1):
    ans = max(ans, time[i][X] + time[X][i]) # i~X, X~i 둘 다 고려해야함

print(ans)