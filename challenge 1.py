class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def find_trail(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        trails = []
        for node in self.graph[start]:
            if node not in path:
                new_trails = self.find_trail(node, end, path)
                trails.extend(new_trails)
        return trails
    
    def find_all_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                paths.extend(new_paths)
        return paths
    
    def find_cycles(self, start, path=None, cycles=None):
        if path is None:
            path = []
        if cycles is None:
            cycles = []
        
        path.append(start)
        for neighbor in self.graph[start]:
            if neighbor == path[0] and len(path) > 2:
                cycles.append(path[:])
            elif neighbor not in path:
                self.find_cycles(neighbor, path[:], cycles)
        return cycles

# Membuat graf berdasarkan gambar
G = Graph()
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')

# Mencari hasil sesuai soal
trail_A_D = G.find_trail('A', 'D')
all_paths_A_D = G.find_all_paths('A', 'D')
cycles_from_A = G.find_cycles('A')

print("Trail dari A ke D:", trail_A_D)
print("Semua path dari A ke D:", all_paths_A_D)
print("Semua siklus yang berawal dari A:", cycles_from_A)