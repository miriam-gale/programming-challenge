# Question 6 - Top 3 Shortest Paths

graph = {}

# Open the file and read the data
with open("ghana_cities_graph_2026.txt", "r") as file:
    for line in file:
        parts = line.split(",")
        source = parts[0].strip()
        destination = parts[1].strip()
        distance = int(parts[2].strip())
        time = int(parts[3].strip())

        # Creates a space for each town if it does not exist
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []

        # Appends the distance, time and neighbour to the space
        graph[source].append((destination, distance, time))
        graph[destination].append((source, distance, time))


# Dijkstra - finds shortest path between two towns
def dijkstra(start, destination):

    distances = {}
    for town in graph:
        distances[town] = float('inf')
    distances[start] = 0

    previous = {}
    for town in graph:
        previous[town] = None

    queue = [(0, start)]

    while queue:
        current_distance, current_town = min(queue)
        queue.remove((current_distance, current_town))

        if current_town == destination:
            break

        for neighbor, dist, time in graph[current_town]:
            new_distance = current_distance + dist

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_town
                queue.append((new_distance, neighbor))

    path = []
    current = destination

    while current != None:
        path.append(current)
        current = previous[current]

    path = path[::-1]

    return path, distances[destination]


# Finds the top 3 shortest paths by temporarily removing roads
def top_3_paths(start, destination):

    all_paths = []

    # Get the first shortest path
    path1, dist1 = dijkstra(start, destination)
    all_paths.append((dist1, path1))

    # Remove one road at a time from path1 and find alternative routes
    for i in range(len(path1) - 1):
        town_a = path1[i]
        town_b = path1[i + 1]

        # Temporarily remove the road between town_a and town_b
        graph[town_a] = [(n, d, t) for n, d, t in graph[town_a] if n != town_b]
        graph[town_b] = [(n, d, t) for n, d, t in graph[town_b] if n != town_a]

        # Run Dijkstra again without that road
        new_path, new_dist = dijkstra(start, destination)

        # Only save this path if a real route was found
        # If no route exists Dijkstra returns infinity so we skip it
        if new_dist != float('inf'):
            all_paths.append((new_dist, new_path))

        # Put the road back
        graph[town_a].append((town_b, dist1, 0))
        graph[town_b].append((town_a, dist1, 0))

    # Sort all paths by distance
    def get_distance(item):
        return item[0]

    all_paths.sort(key=get_distance)

    # Remove duplicate paths
    seen = []
    unique_paths = []
    for dist, path in all_paths:
        if path not in seen:
            seen.append(path)
            unique_paths.append((dist, path))

    # Print the top 3
    print("Top 3 Shortest Paths from", start_town, "to", destination_town)

    for rank in range(min(3, len(unique_paths))):
        dist, path = unique_paths[rank]
        route = " -> ".join(path)
        print("\nPath", rank + 1)
        print("Route:   ", route)
        print("Distance:", str(dist) + " km")


start_town = input("Enter start town: ")
destination_town = input("Enter destination town: ")
top_3_paths(start_town, destination_town)