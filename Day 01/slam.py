import networkx as nx
import folium

# Graph create karna
graph = nx.Graph()  # ✅ Fix: Graph ka object create kiya

# Waypoints
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

# Edges define karna
edges = [
    ("Main Gate", "Security Cabin"),
    ("Security Cabin", "dummy point 1"),
    ("dummy point 1", "Civil Block"),
    ("dummy point 1", "dummy point 2"),
    ("dummy point 2", "EEE Block"),
    ("dummy point 2", "dummy point 3"),
    ("dummy point 3", "CSE & IT Block"),
    ("dummy point 3", "dummy point 4"),
    ("dummy point 4", "ECE Block"),
    ("dummy point 4", "dummy point 3"),
    ("dummy point 3", "dummy point 2"),
    ("dummy point 2", "dummy point 1"),
    ("dummy point 1", "Security Cabin"),
]

# Graph me edges add karna
graph.add_edges_from(edges)  # ✅ Fix: Ab error nahi aayega

# Source aur Target Nodes
source = "Main Gate"
target = "ECE Block"

# Shortest Path nikalna
shortest_path = nx.shortest_path(graph, source=source, target=target)

# Shortest path ka coordinate list
selected_path = [waypoints[node] for node in shortest_path] if shortest_path else []

# Map generate karne ka function
def generate_map():
    start_location = waypoints[source]

    folium_map = folium.Map(location=start_location, zoom_start=18)  # ✅ Fix: folium_Map → folium.Map

    for name, coord in waypoints.items():
        folium.Marker(coord, popup=name, icon=folium.Icon(color="blue")).add_to(folium_map)  # ✅ Fix: folium.icon → folium.Icon

    if selected_path:
        folium.PolyLine(selected_path, color="red", weight=5, opacity=0.8).add_to(folium_map)  # ✅ Fix: folium.polyLine → folium.PolyLine

        folium.Marker(selected_path[0], popup="Start: " + source, icon=folium.Icon(color="green")).add_to(folium_map)
        folium.Marker(selected_path[-1], popup="Destination: " + target, icon=folium.Icon(color="red")).add_to(folium_map)  # ✅ Fix: source → target

    folium_map.save("map.html")  # ✅ Fix: Path correct hai
    
generate_map()



