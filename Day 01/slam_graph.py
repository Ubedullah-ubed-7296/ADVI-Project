import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# 📍 Waypoints (Nodes with coordinates)
waypoints = {
    "Main Gate": (17.281721, 78.537373),
    "Civil Block": (17.281419, 78.538140),
    "EEE Block": (17.281386, 78.538607),
    "CSE & IT Block": (17.281378, 78.539168),
    "ECE Block": (17.281396, 78.539471),
    "Security Cabin": (17.281712, 78.537494),
    "dummy point 1": (17.281693, 78.538132),
    "dummy point 2": (17.281670, 78.538620),
    "dummy point 3": (17.281642, 78.539146),
    "dummy point 4": (17.281632, 78.539532)
}

# 🔗 Edges (Connections)
edges = [
    ("Main Gate", "Security Cabin"),
    ("Security Cabin", "dummy point 1"),
    ("dummy point 1", "Civil Block"),
    ("dummy point 1", "dummy point 2"),
    ("dummy point 2", "EEE Block"),
    ("dummy point 2", "dummy point 3"),
    ("dummy point 3", "CSE & IT Block"),
    ("dummy point 3", "dummy point 4"),
    ("dummy point 4", "ECE Block")
]

# 🛠 Create Graph
graph = nx.Graph()
graph.add_nodes_from(waypoints.keys())  # Nodes
graph.add_edges_from(edges)  # Edges

# 🔍 Find Shortest Path
source = "Main Gate"
target = "ECE Block"
shortest_path = nx.shortest_path(graph, source=source, target=target)
selected_path = [waypoints[node] for node in shortest_path] if shortest_path else []

# 🏃‍♂️ Function to Generate Interpolated Points
def interpolate(start, end, steps=20):
    lat_diff = (end[0] - start[0]) / steps
    lng_diff = (end[1] - start[1]) / steps
    return [(start[0] + i * lat_diff, start[1] + i * lng_diff) for i in range(steps + 1)]  

# 🛤 Get All Movement Steps
movement_steps = []
for i in range(len(selected_path) - 1):
    movement_steps.extend(interpolate(selected_path[i], selected_path[i + 1]))

# 🎥 Animation Setup
fig, ax = plt.subplots(figsize=(6, 6))

# Convert waypoints to a position dictionary for plotting
pos = {node: (coords[1], coords[0]) for node, coords in waypoints.items()}  # Lat, Long swapped
nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=8)

# Initialize marker for movement
marker, = plt.plot([], [], 'ro', markersize=10)  # 'ro' = red circle

# 🔄 Animation Update Function
def update(frame):
    lat, lng = movement_steps[frame]
    marker.set_data(lng, lat)
    return marker,

# 🚀 Run Animation
ani = animation.FuncAnimation(fig, update, frames=len(movement_steps), interval=200, repeat=False)
plt.title("Simulated Movement on Shortest Path")
plt.show()
