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
    
    def find_shortest_longest_circuit(self, start, end):
        all_paths = self.find_all_paths(start, end)
        if not all_paths:
            return None, None
        shortest = min(all_paths, key=len)
        longest = max(all_paths, key=len)
        return shortest, longest

# Membuat graf berdasarkan gambar untuk Challenge 2
G = Graph()
G.add_edge('A', 'B')
G.add_edge('A', 'D')
G.add_edge('B', 'C')
G.add_edge('B', 'D')
G.add_edge('B', 'E')
G.add_edge('C', 'E')
G.add_edge('C', 'F')
G.add_edge('D', 'E')
G.add_edge('E', 'F')

# Mencari hasil sesuai soal
all_paths_A_C = G.find_all_paths('A', 'C')
cycles_from_A = G.find_cycles('A')
cycles_from_B = G.find_cycles('B')
shortest_circuit, longest_circuit = G.find_shortest_longest_circuit('A', 'C')

print("Semua path dari A ke C:", all_paths_A_C)
print("Semua siklus yang berawal dari A:", cycles_from_A)
print("Semua siklus yang berawal dari B:", cycles_from_B)
print("Circuit terpendek dari A ke C:", shortest_circuit)
print("Circuit terpanjang dari A ke C:", longest_circuit)
