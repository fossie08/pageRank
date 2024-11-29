def calculate_pagerank(graph, damping_factor=0.85, max_iterations=5, tol=1.0e-6):
    nodes = list(graph.keys())
    num_nodes = len(nodes)
    pagerank = {node: 1 / num_nodes for node in nodes}

    for iteration in range(max_iterations):
        new_pagerank = {}
        for node in nodes:
            inbound_links = [n for n in nodes if node in graph[n]]
            rank_sum = sum(pagerank[link] / len(graph[link]) for link in inbound_links)
            new_pagerank[node] = (1 - damping_factor) + damping_factor * rank_sum

        diff = sum(abs(new_pagerank[node] - pagerank[node]) for node in nodes)
        pagerank = new_pagerank
        if diff < tol:
            break

    return pagerank


if __name__ == "__main__":
    graph = {
        "Home": ['Login','Contact'],
        "Contact": ['Home'],
        "Login": ['Contact'],
    }

    pagerank = calculate_pagerank(graph)
    print("PageRank Results:")
    for node, rank in pagerank.items():
        print(f"{node}: {rank:.4f}")
