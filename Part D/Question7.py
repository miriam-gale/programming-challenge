# Question 7 - Fuel Cost

# Given constants from the question
FUEL_CONSUMPTION = 8
FUEL_PRICE = 11.95

# Build the graph
graph = {}

with open("ghana_cities_graph_2026.txt", "r") as file:
    for line in file:
        parts = line.split(",")
        source = parts[0].strip()
        destination = parts[1].strip()
        distance = int(parts[2].strip())
        time = int(parts[3].strip())

        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []

        graph[source].append((destination, distance, time))
        graph[destination].append((source, distance, time))


# Dijkstra - finds the shortest distance path between two towns
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


# Calculates the fuel cost of a route using its distance
def fuel_cost(distance):
    litres_used = distance / FUEL_CONSUMPTION
    distance_cost = litres_used * FUEL_PRICE
    return distance_cost


# --- Run ---
start = input("Enter start town: ")
destination = input("Enter destination town: ")

path, total_distance = dijkstra(start, destination)

route = " -> ".join(path)
fuel = "GHS " + str(round(fuel_cost(total_distance), 2))

print("\nRoute:     ", route)
print("Distance:  ", str(total_distance) + " km")
print("Fuel Cost: ", fuel)