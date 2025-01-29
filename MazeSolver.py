def find_exit(graph, start, finish):
    def DFS(node):
        visited.add(node)
        path.append(node)
        if node == finish:
            print(f"Found path to exit: {' -> '.join(str(i) for i in path)}")
            return
        for neighbor in graph[node]:
            if neighbor not in visited:
                DFS(neighbor)
        path.pop()
    
    visited = set()
    path = []
    
    DFS(start)

def main():
    graph = {
        1 : [2, 6],
        2 : [1, 3],
        3 : [2, 8],
        4 : [5],
        5 : [4, 10],
        6 : [1, 11],
        7 : [8],
        8 : [3, 7],
        9 : [10, 14],
        10 : [5, 9, 15],
        11 : [6, 12],
        12 : [11, 17],
        13 : [14],
        14 : [9, 13, 19],
        15 : [10, 20],
        16 : [17],
        17 : [12, 16, 18],
        18 : [17, 19],
        19 : [14, 18],
        20 : [15]
    }
    
    find_exit(graph, 2, 5)

if __name__=="__main__":
    main()