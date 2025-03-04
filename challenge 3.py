# Representasi graf berdasarkan gambar
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'G'],
    'C': ['A', 'E', 'F'],
    'D': ['A', 'F'],
    'E': ['B', 'C', 'H', 'F'],
    'F': ['C', 'D', 'E', 'I'],
    'G': ['B', 'H'],
    'H': ['E', 'G', 'I', 'K'],
    'I': ['F', 'H', 'J', 'K'],
    'J': ['I', 'K'],
    'K': ['H', 'I', 'J'],
}

# Fungsi untuk mencari semua path dari start ke end menggunakan DFS
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    
    paths = []
    for node in graph[start]:
        if node not in path:  # Hindari siklus
            new_paths = find_all_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths

# Fungsi untuk menemukan semua siklus (cycle) yang dimulai dari start
def find_cycles(graph, start, current, visited, path):
    path.append(current)
    visited.add(current)

    cycles = []
    for neighbor in graph[current]:
        if neighbor == start and len(path) > 2:  # Menemukan siklus yang kembali ke awal
            cycles.append(path + [start])
        elif neighbor not in visited:
            cycles.extend(find_cycles(graph, start, neighbor, visited.copy(), path[:]))

    return cycles

# Fungsi untuk mencari semua siklus dari titik awal tertentu
def get_cycles(graph, start):
    return find_cycles(graph, start, start, set(), [])

# Fungsi untuk mencari sirkuit terpendek dan terpanjang dari titik tertentu
def find_shortest_and_longest_circuit(graph, start):
    cycles = get_cycles(graph, start)
    if not cycles:
        return None, None
    shortest = min(cycles, key=len)
    longest = max(cycles, key=len)
    return shortest, longest

# Menampilkan hasil sesuai pertanyaan pada gambar
print("1. Semua kemungkinan path dari A ke K:", find_all_paths(graph, 'A', 'K'))
print("2. Semua kemungkinan path dari E ke J:", find_all_paths(graph, 'E', 'J'))
print("3. Semua kemungkinan path dari E ke F:", find_all_paths(graph, 'E', 'F'))
print("4. Semua kemungkinan cycle jika A adalah titik awal:", get_cycles(graph, 'A'))
print("5. Semua kemungkinan cycle jika K adalah titik awal:", get_cycles(graph, 'K'))

shortest_circuit_A, longest_circuit_A = find_shortest_and_longest_circuit(graph, 'A')
print("6. Circuit terpendek dari A:", shortest_circuit_A)
print("7. Circuit terpendek dari J:", find_shortest_and_longest_circuit(graph, 'J')[0])
print("8. Circuit terpendek dari F:", find_shortest_and_longest_circuit(graph, 'F')[0])
