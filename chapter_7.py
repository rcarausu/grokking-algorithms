"""
7. DIJKSTRA'S ALGORITHM

It works with weighted graphs, where each edge has a weight.
BFS fins the lowest number of segments for a bath, Dijkstra's finds the fastest path instead.

Working with Dijkstra's Algorithm

4 steps
1. Find the 'cheapest' node.
2. Update the cost of its neighbors. Check fi there's a cheaper path to the neighbors of the node, if so,
update its cost.
3. Repeat for every node in the graph.
4. Calculate the final path.

Dijkstra's only works with DAG (Directed Acyclic Graphs), and it can't be used with negative weight edges.

To find the shortest path for negative weight edges, we can use the 'Bellman-Ford' algorithm, which is out of the
scope of this book.

Implementation

We need 3 hash tables. One for representing the graph (hash table of hash tables, since for each node we also store
its weight), another for the costs and another for the parents.

We also need an array to keep track of processed nodes.

while we have nodes to process
            ||
grab the node that is closest to the start
            ||
update the costs for its neighbors
            ||
if any of the neighbors costs were updated,
update the parents too
            ||
mark this node as processed and go to step 1

"""
from typing import List, Dict, Tuple


def find_lowest_cost_node(costs: Dict, processed_nodes: List[str]):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        # If it''s lowest cost so far & hasn't been processed yet, set as lowest_cost_node
        if cost < lowest_cost and node not in processed_nodes:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph: Dict, costs: Dict, parents: Dict) -> Tuple[Dict, Dict]:
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return costs, parents


def path_from_parents(parents: Dict, start_node: str, end_node: str) -> List[str]:
    current = end_node

    if start_node == end_node:
        return [end_node]

    path = []
    while current != start_node:
        for p in parents.keys():
            if p == current:
                path.append(current)
                current = parents[p]
    path.append(start_node)
    path.reverse()
    return path


if __name__ == '__main__':
    # Example with graph from page 131 of the book
    graph = dict()
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    graph['a'] = dict()
    graph['a']['fin'] = 1
    graph['b'] = dict()
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    graph['fin'] = dict()  # finish node doesn't have any neighbors

    # we add the costs hash table with all the nodes of the graph (except the start),
    # with infinity for the costs we don't know yet
    infinity = float('inf')
    costs = dict()
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = infinity

    # we add the parents hash table, we need it to calculate the final path,with None for the parents we don't know yet
    parents = dict()
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None

    dijkstra(graph, costs, parents)
    print(f"graph: {graph}")
    print(f"costs: {costs}")
    print(f"parents: {parents}")
    print(
        f"Shortest path is {path_from_parents(parents, start_node='start', end_node='fin')} with a total cost of {costs['fin']}")
