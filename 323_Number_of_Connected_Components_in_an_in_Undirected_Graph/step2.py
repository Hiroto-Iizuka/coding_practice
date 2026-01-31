class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_to_neighbor = {i: [] for i in range(n)}
        for u, v in edges:
            node_to_neighbor[u].append(v)
            node_to_neighbor[v].append(u)
        
        visited = set()
        count = 0
        
        for i in range(n):
            if i not in visited:
                self.explore_component(i, visited, node_to_neighbor)
                count += 1
        
        return count

    def explore_component(self, node, visited, node_to_neighbor):
        visited.add(node)
        for neighbor in node_to_neighbor[node]:
            if neighbor not in visited:
                self.explore_component(neighbor, visited, node_to_neighbor)
                