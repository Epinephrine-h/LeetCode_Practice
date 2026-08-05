class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in invocations:
            graph[u].append(v)
        def dfs(u):
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:      dfs(v)
        dfs(k)
        for u, v in invocations:
            if not visited[u] and visited[v]:   return list(range(n))
        return list(u for u in range(n) if not visited[u])