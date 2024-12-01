from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    #Key start, Value : next station
    for a,b in tickets:
        graph[a].append(b)

    #ICN, HND, JFK가 key가 되는 구조
    for key in graph.keys():
        graph[key].sort()
    print("Graph Value")
    print(graph)
    return dfs(graph, ["ICN"], [])

def dfs(graph, path, visit):
    print("-BEFORE PATH-")
    print(path)
    if path:
        to = path[-1]
        if graph[to]: #다른 연결 도착 지점이 있는 경우(티켓이 두장이라면 몰라도 이 경우는 없다.)
            next_station = graph[to].pop(0) #pop left side item: 근데 문제는 티켓이 1방향이다. 즉, 리스트의 크기가 1을 넘을 수 없다.
            print(next_station)
            print("-AFTER PATH-")
            path.append(next_station) #Just 방문 경로에 등록함.
            print(path)
        else:
            print(f"Final node {to} -> {graph[to]}")
            visit_station = path.pop(0)
            print(f"Visit station {visit_station}")
            visit.append(visit_station)
        dfs(graph, path, visit)
    return visit[::-1]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
rtn_path = solution(tickets)
print(rtn_path)