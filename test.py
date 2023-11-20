from collections import deque
import heapq

def remove_recursive(node, word, index ):
    if index == len(word):
        if node.end_word is False:
            return False
        node.end_word = True
        return len(node.children) == 0

    char = word[index]
    if word[index] not in  node.children:
        return False
    
    should_delete = remove_recursive(node.children, word, index + 1)

    if should_delete :
        del node.children[char]
        return len(node.children) == 0
    
    return False

def remove(tree, word):
    remove_recursive(tree, word, 0)

def dfs(tree, start, visited=None):
    if visited is None:
        visited = []
    if start not in tree:
        return []
    if start not in visited:
        visited.append(start)
        for neighbour in tree[start]:
            dfs(tree, neighbour, visited) 
    
    for key in tree:
        if key not in visited:
            dfs(tree, key, visited)

    return visited

def bfs(tree, start, visited = None):
    if visited is None:
        visited = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(tree[vertex])
    
    for vertex in tree:
        if vertex not in visited:
            bfs(tree, vertex, visited)


def dijikstra(graph, start, end):
    priority_queue = [(0,start)]
    distances = {vertex : float('inf') for vertex in graph}
    previous = {vertex : None for vertex in graph}  
    distances[start] = 0

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbour, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distances
                previous[neighbour] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbour)) 
