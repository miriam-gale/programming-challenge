# Question 7 - Fuel Cost

# Given constants from the question
FUEL_CONSUMPTION = 8      # km per litre
FUEL_PRICE       = 11.95  # GHS per litre

# Build the graph
graph = {}

with open("ghana_cities_graph_2026.txt", "r") as file:
    for line in file:
        parts       = line.split(",")
        source      = parts[0].strip()
        destination = parts[1].strip()
        distance    = int(parts[2].strip())
        time        = int(parts[3].strip())

        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []

        graph[source].append((destination, distance, time))
        graph[destination].append((source, distance, time))


# Dijkstra using min() - returns path and total distance
def dijkstra(start, destination):

    distances = {town: float('inf') for town in graph}
    distances[start] = 0
    previous  = {town: None for town in graph}
    queue     = [(0, start)]

    while queue:
        current_distance, current_town = min(queue)
        queue.remove((current_distance, current_town))

        if current_town == destination:
            break

        for neighbor, dist, time in graph[current_town]:
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


# Question 7 - Calculates the fuel cost of a route using its distance
def fuel_cost(distance):
    # Formula: (Distance / 8) x Fuel Price
    distance_cost = (distance / FUEL_CONSUMPTION) * FUEL_PRICE
    return distance_cost


# --- Run ---
start       = input("Enter start town: ")
destination = input("Enter destination town: ")

path, total_distance = dijkstra(start, destination)

print("\nRoute    :", " -> ".join(path))
print("Distance :", total_distance, "km")
print("Fuel Cost: GHS", round(fuel_cost(total_distance), 2))