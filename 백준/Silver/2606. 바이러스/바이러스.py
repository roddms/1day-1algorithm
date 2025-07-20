N = int(input()) # 정점의 수
M = int(input()) # 간선의 수

g = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (N+1)
cnt = 0

def solve_dfs(node):
    global g, visited, cnt

    if visited[node]==True:
        return
    
    visited[node] = True
    cnt += 1

    for g_node in g[node]:
        solve_dfs(g_node)


solve_dfs(1)
print(cnt-1)