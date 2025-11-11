from collections import defaultdict

def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
        
    for airport in graph:
        graph[airport].sort(reverse=True)
        
    tmp = ['ICN'] # 현재까지 지나온 경로를 담는 임시 리스트
    
    while tmp:
        route = tmp[-1]
        
        if not graph[route]:
            answer.append(tmp.pop())
        
        else:
            tmp.append(graph[route].pop())
            
    
    return answer[::-1]