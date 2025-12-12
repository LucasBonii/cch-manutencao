from __future__ import annotations

from queue import Queue


class Graph:
    def __init__(self) -> None:
        self.vertices: dict[int, list[int]] = {}

    def print_graph(self) -> None:
        """
        prints adjacency list representation of graaph
        >>> g = Graph()
        >>> g.print_graph()
        >>> g.add_edge(0, 1)
        >>> g.print_graph()
        0  :  1
        """
        for i in self.vertices:
            print(i, " : ", " -> ".join([str(j) for j in self.vertices[i]]))

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """
        adding the edge between two vertices
        >>> g = Graph()
        >>> g.print_graph()
        >>> g.add_edge(0, 1)
        >>> g.print_graph()
        0  :  1
        """
        if from_vertex in self.vertices:
            self.vertices[from_vertex].append(to_vertex)
        else:
            self.vertices[from_vertex] = [to_vertex]

    def bfs(self, start_vertex: int) -> set[int]:
        """
        Performs Breadth-First Search (BFS) to find all reachable vertices.
        
        Args:
            start_vertex: Initial vertex of the search
            
        Returns:
            Set of visited vertices
        """
        # Set of vertices already visited
        visited_vertices: set[int] = set()
        
        # FIFO queue for level-by-level processing
        bfs_queue: Queue[int] = Queue()
        
        # It starts with the starting vertex.
        visited_vertices.add(start_vertex)
        bfs_queue.put(start_vertex)
        
        while not bfs_queue.empty():
            current_vertex = bfs_queue.get()
            
            # Explore unvisited neighbors
            for neighbor_vertex in self.vertices.get(current_vertex, []):
                if neighbor_vertex not in visited_vertices:
                    visited_vertices.add(neighbor_vertex)
                    bfs_queue.put(neighbor_vertex)
        
        return visited_vertices


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.print_graph()
    # 0  :  1 -> 2
    # 1  :  2
    # 2  :  0 -> 3
    # 3  :  3

    assert sorted(g.bfs(2)) == [0, 1, 2, 3]