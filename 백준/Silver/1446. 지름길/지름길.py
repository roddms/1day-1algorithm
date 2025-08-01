from queue import PriorityQueue

N, D = map(int, input().split())
adj_lst = [[] for _ in range(D + 2)]

for _ in range(N):
    s, d, l = map(int, input().split())  # 출발지, 도착지, 길의 길이
    if d <= D and l < d - s:
        adj_lst[s].append((d, l)) 

INF = int(1e12)
dist = [INF] * (D + 2)

pq = PriorityQueue()
pq.put((0, 0))
dist[0] = 0

while not pq.empty():
    cur_dist, cur_pos = pq.get()

    if cur_dist > dist[cur_pos]:
        continue

    for adj_pos, adj_dist in adj_lst[cur_pos]:
        tmp_dist = cur_dist + adj_dist

        if tmp_dist < dist[adj_pos]:
            dist[adj_pos] = tmp_dist
            pq.put((tmp_dist, adj_pos)) 

    # 일반 도로로 한 칸 이동
    if cur_pos + 1 <= D and dist[cur_pos + 1] > cur_dist + 1:
        dist[cur_pos + 1] = cur_dist + 1
        pq.put((cur_dist + 1, cur_pos + 1)) 

print(dist[D])
