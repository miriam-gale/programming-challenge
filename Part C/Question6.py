# Question 6


graph = {}

#  Open the file and read the data
with open("ghana_cities_graph_2026.txt", "r") as file:
    for line in file:
        parts       = line.split(",")
        source      = parts[0].strip()
        destination = parts[1].strip()
        distance    = int(parts[2].strip())
        time        = int(parts[3].strip())

        #  Ceates a space for each toen if it does not exist
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []

        # Appends the distance, time and neighbour to the space
        graph[source].append((destination, distance, time))
        graph[destination].append((source, distance, time))


# Dijkstra using min()
def dijkstra(start, destination):
    # Only save this new path if a real route was found
    # If no route exists, Dijkstra returns infinity(which means the path does not exist) so we skip it
    distances = {town: float('inf') for town in graph}
    distances[start] = 0
    previous = {town: None for town in graph}
    queue = [(0, start)]

    while queue:
        # Pick the town with the smallest distance using min()
        current_distance, current_town = min(queue)
        queue.remove((current_distance, current_town))

        if current_town == destination:
            break

        for neighbor, dist in graph[current_town]:
            new_distance = current_distance + dist

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor]  = current_town
                queue.append((new_distance, neighbor))

    # Rebuild path
    path    = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return path, distances[destination]


# Top 3 shortest paths
def top_3_paths(start, destination):

    all_paths = []

    # Get first shortest path
    path1, dist1 = dijkstra(start, destination)
    all_paths.append((dist1, path1))

    # Remove one road at a time from path1 and find alternative routes
    for i in range(len(path1) - 1):
        town_a = path1[i]
        town_b = path1[i + 1]

        # Temporarily remove the road
        graph[town_a] = [(n, d, t) for n, d, t in graph[town_a] if n != town_b]
        graph[town_b] = [(n, d, t) for n, d, t in graph[town_b] if n != town_a]

        # Run Dijkstra without that road
        new_path, new_dist = dijkstra(start, destination)

        if new_dist != float('inf'):
            all_paths.append((new_dist, new_path))

        # Put the road back
        graph[town_a].append((town_b, dist1, 0))
        graph[town_b].append((town_a, dist1, 0))

    # Sort by distance and remove duplicates
    all_paths.sort(key=lambda x: x[0])
    seen         = []
    unique_paths = []
    for dist, path in all_paths:
        if path not in seen:
            seen.append(path)
            unique_paths.append((dist, path))

    # Print top 3
    print("Top 3 Shortest Paths from", start, "to", destination)
    print("-" * 50)
    for rank in range(min(3, len(unique_paths))):
        dist, path = unique_paths[rank]
        print(f"\nPath {rank + 1}:")
        print("  Route    :", " -> ".join(path))
        print("  Distance :", dist, "km")


start       = input("Enter start town: ")
destination = input("Enter destination town: ")
top_3_paths(start, destination)