from SmartKart.src.pathfinding.store_graph import StoreGraph

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
