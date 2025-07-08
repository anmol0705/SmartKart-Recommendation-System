import networkx as nx

class StoreGraph:
    def __init__(self):
        self.G = nx.Graph()

    def add_location(self, node_id: str, label: str = "", products=None):
        """
        Add a store node with a label and optional product list.

        Args:
            node_id (str): Unique ID for the location.
            label (str): Human-readable name (e.g., 'Dairy')A.
            products (List[int]): List of product IDs available at this node.
        """
        if products is None:
            products = []
        self.G.add_node(node_id, label=label, products=products)

    def add_path(self, from_id: str, to_id: str, distance: float = 1.0):
        """
        Add a bidirectional path between store locations.

        Args:
            from_id (str): Starting location.
            to_id (str): Ending location.
            distance (float): Distance or time cost between them.
        """
        self.G.add_edge(from_id, to_id, weight=distance)

    def shortest_path(self, source: str, target: str):
        """
        Basic shortest path based on distance only.

        Args:
            source (str): Start node.
            target (str): End node.

        Returns:
            dict: Path list and total distance.
        """
        try:
            path = nx.shortest_path(self.G, source=source, target=target, weight='weight')
            total_dist = nx.shortest_path_length(self.G, source=source, target=target, weight='weight')
            return {"path": path, "distance": total_dist}
        except nx.NetworkXNoPath:
            return {"path": None, "distance": float('inf')}

    def smart_shortest_path(self, source: str, target: str, recommended_ids: list, lambda_boost=2.0):
        """
        Path that prioritizes recommended product locations by reducing edge weights.

        Args:
            source (str): Start node.
            target (str): End node.
            recommended_ids (list[int]): Product IDs to favor.
            lambda_boost (float): Boost factor for preferred paths.

        Returns:
            dict: Smart path and effective cost.
        """
        G = self.G.copy()

        # Assign scores to nodes based on whether they contain recommended products
        node_scores = {
            n: int(any(pid in G.nodes[n].get("products", []) for pid in recommended_ids))
            for n in G.nodes()
        }

        # Adjust edge weights to bias towards high-score nodes
        for u, v, data in G.edges(data=True):
            base = data.get("weight", 1.0)
            boost = lambda_boost * node_scores.get(v, 0)
            G[u][v]["weight"] = base - boost  # negative boost = shorter effective path

        try:
            path = nx.shortest_path(G, source=source, target=target, weight='weight')
            cost = nx.path_weight(G, path, weight="weight")
            return {"path": path, "smart_cost": cost}
        except nx.NetworkXNoPath:
            return {"path": None, "smart_cost": float('inf')}

    def visualize(self):
        """
        Visualize the store graph.
        """
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(self.G)
        labels = nx.get_node_attributes(self.G, 'label')
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', node_size=1000)
        nx.draw_networkx_labels(self.G, pos, labels=labels)
        plt.show()



# Test

# from graph_build import StoreGraph
store = StoreGraph()

store.add_location("A1", "Entrance")
store.add_location("A2", "Snacks", products=[101, 202])
store.add_location("A3", "Drinks", products=[303])
store.add_location("A4", "Dairy", products=[404, 505])
store.add_location("A5", "Exit")

store.add_path("A1", "A2", 2)
store.add_path("A2", "A3", 3)
store.add_path("A3", "A4", 3)
store.add_path("A4", "A5", 2)
store.add_path("A2", "A4", 6)

# Normal path
print("Shortest Path:", store.shortest_path("A1", "A5"))

# Smart path with product boost
recommended_items = [202, 303, 505]
print("Smart Path:", store.smart_shortest_path("A1", "A5", recommended_items))
