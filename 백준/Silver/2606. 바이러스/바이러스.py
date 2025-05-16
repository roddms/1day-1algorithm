N = int(input())
M = int(input())

adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

# 인접 리스트 만들기
for i in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# dfs 구현
def solve_dfs(node):
    global cnt
    visited[node] = True

    for adj_node in adj_list[node]:
        if not visited[adj_node]:
            cnt += 1
            solve_dfs(adj_node)
    
 
# solve
solve_dfs(1)
print(cnt)