"""
6. BREADTH-FIRST SEARCH (BFS)

Allows to find the shortest path (number of edges) between two nodes in a graph.
It's a graph algorithm.

(A) ---> (B)

A and B are nodes, ---> is the edge between them.
Edges can be directed (arrow) or undirected (no arrow).

In this second case, it means that both nodes point o each-other, it is equivalent to (A) <---> (B).

BFS can answer 2 types of questions:
1. Is there a path from node A to B.
2. What is the lowest number of edges between A and B.

Search radiates from the start node. First-degree connections are added to the search list before
second-degree connections.

It needs to search on the order the elements are added, to do this it uses 'queues'.

## Queues

They are a basic data structure with 2 operations:
- Enqueue: add an element to the back of the queue.
- Dequeue: remove an element from the start of the queue.

Queues are FIFO data structures (First In, First Out), in contrast to stacks, which are LIFO (Last In, First Out).

In Python, we can use hash tables (dictionaries) to implement a graph. Hash tables have no order, so it doesn't
matter the order in which we add the nodes.

## Algorithm

1. Keep a queue containing the nodes to check.
2. Pop (dequeue) a node off the queue.
3. Check if node is expected.
    4a. Yes --> we're done.
    4b. No --> add all their neighbors to the queue.
5. Loop to point 2.
6. If the queue is empty, the expected node isn't in the graph.

To avoid duplicates and infinite loops, we need to mark already processed nodes in a separate array.

## Performance

If we search an entire network, we'll follow each ege, so Oedges).
We also keep a queue of every node to search. Adding one node is O(1), adding all nodes is O(#nodes).

So breadth-frist search takes O(#nodes * #edges), commonly expressed as O(V+E), where V = vertices and E = edges.
"""

# python has an implementation for queues
from collections import deque


def bfs_search(graph: dict, start_node: str, end_node: str) -> bool:
    search_queue = deque()
    search_queue += graph[start_node]
    searched = set()  # keep track of searches
    while search_queue:
        current_node = search_queue.popleft()
        if not current_node in searched:
            if current_node == end_node:
                return True
            else:
                search_queue += graph[current_node]
                searched.add(current_node)
    return False


def bfs_shortest_path(graph: dict, start_node: str, end_node: str) -> list:
    explored = set()
    queue = deque()
    # we use a queue of paths, we explore each possible path until we find the end node, then return that path
    queue.append([start_node])

    if start_node == end_node:
        return [start_node]

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in explored:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == end_node:
                    return new_path
            explored.add(node)
    raise Exception('No paths found!')


if __name__ == '__main__':
    # graph from bottom of page 105 of the book
    graph = dict()
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    # is there a person that it's name ends with 'm'?
    print(bfs_search(graph, 'you', 'thom'))  # it will return True, since 'thom' ends with 'm'.

    print(bfs_shortest_path(graph, start_node='you', end_node='thom'))
