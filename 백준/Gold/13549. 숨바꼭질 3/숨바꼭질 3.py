from queue import PriorityQueue

N, K = map(int, input().split())
INF = int(1e12)
time = [INF] * (100001)

pq = PriorityQueue()
pq.put([0, N])
time[N] = 0

while not pq.empty():
    cur_time, cur_pos = pq.get()

    nxt = ([cur_time+1, cur_pos+1],[cur_time+1, cur_pos-1], [cur_time, cur_pos*2])

    for nxt_time, nxt_pos in nxt:
        if (0<= nxt_pos <= 100000) and (nxt_time < time[nxt_pos]):
            time[nxt_pos] = nxt_time
            pq.put([nxt_time, nxt_pos])

print(time[K])