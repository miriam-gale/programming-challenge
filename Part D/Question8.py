# Question 8 - Total Cost and Recommendation

# Given constants from the question
FUEL_CONSUMPTION = 8      # km per litre
FUEL_PRICE       = 11.95  # GHS per litre
TIME_COST        = 0.5    # GHS per minute

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


# Dijkstra that works for both distance and time depending on mode
def dijkstra(start, destination, mode):

    costs    = {town: float('inf') for town in graph}
    costs[start] = 0
    previous = {town: None for town in graph}
    queue    = [(0, start)]

    while queue:
        current_cost, current_town = min(queue)
        queue.remove((current_cost, current_town))

        if current_town == destination:
            break

        for neighbor, dist, time in graph[current_town]:

            # Use distance or time as the weight depending on the mode
            if mode == "distance":
                weight = dist
            else:
                weight = time

            new_cost = current_cost + weight

            if new_cost < costs[neighbor]:
                costs[neighbor]    = new_cost
                previous[neighbor] = current_town
                queue.append((new_cost, neighbor))

    # Rebuild path
    path    = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return path, costs[destination]


# Calculates fuel cost from distance
def fuel_cost(distance):
    return (distance / FUEL_CONSUMPTION) * FUEL_PRICE


# Calculates total cost from distance and time
def total_cost(distance, time):
    # Formula: distance_cost + (Time x 0.5)
    return fuel_cost(distance) + (time * TIME_COST)


# Manually adds up distance or time along any given path
def path_stats(path, stat):
    total = 0
    for i in range(len(path) - 1):
        town_a = path[i]
        town_b = path[i + 1]
        for neighbor, dist, time in graph[town_a]:
            if neighbor == town_b:
                # Add distance or time depending on what we want
                if stat == "distance":
                    total += dist
                else:
                    total += time
                break
    return total


# --- Run ---
start       = input("Enter start town: ")
destination = input("Enter destination town: ")

# Get both routes
distance_path, total_distance = dijkstra(start, destination, "distance")
time_path,     total_time     = dijkstra(start, destination, "time")

# Get the missing stat for each path
distance_path_time     = path_stats(distance_path, "time")
time_path_distance     = path_stats(time_path,     "distance")

# Calculate total cost for each route
cost_of_distance_route = total_cost(total_distance,    distance_path_time)
cost_of_time_route     = total_cost(time_path_distance, total_time)

# Print shortest distance route
print("\n--- Shortest Distance Route ---")
print("Route     :", " -> ".join(distance_path))
print("Distance  :", total_distance, "km")
print("Time      :", distance_path_time, "minutes")
print("Fuel Cost : GHS", round(fuel_cost(total_distance), 2))
print("Total Cost: GHS", round(cost_of_distance_route, 2))

# Print fastest time route
print("\n--- Fastest Time Route ---")
print("Route     :", " -> ".join(time_path))
print("Distance  :", time_path_distance, "km")
print("Time      :", total_time, "minutes")
print("Fuel Cost : GHS", round(fuel_cost(time_path_distance), 2))
print("Total Cost: GHS", round(cost_of_time_route, 2))

# Compare and recommend
print("\n--- RECOMMENDATION ---")
if cost_of_distance_route < cost_of_time_route:
    print("Take the Shortest Distance Route")
    print("Reason: It costs GHS", round(cost_of_distance_route, 2), "which is cheaper than GHS", round(cost_of_time_route, 2))
else:
    print("Take the Fastest Time Route")
    print("Reason: It costs GHS", round(cost_of_time_route, 2), "which is cheaper than GHS", round(cost_of_distance_route, 2))