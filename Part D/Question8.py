# Question 8 - Total Cost and Recommendation

# Given constants from the question
FUEL_CONSUMPTION = 8      # km per litre
FUEL_PRICE = 11.95  # GHS per litre
TIME_COST = 0.5    # GHS per minute

# Build the graph
graph = {}

with open("ghana_cities_graph_2026.txt", "r") as file:
    for line in file:
        parts = line.split(",")

        source = parts[0].strip()
        destination = parts[1].strip()
        distance = int(parts[2].strip())
        time = int(parts[3].strip())

        graph[source].append((destination, distance, time))
        graph[destination].append((source, distance, time))


# Dijkstra that works for both distance and time depending on mode
def dijkstra(start, destination, mode):

    costs = {}
    for town in graph:
        costs[town] = float('inf')
    costs[start] = 0

    previous = {}
    for town in graph:
        previous[town] = None

    queue = [(0, start)]

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
    path = []
    current = destination

    while current != None:
        path.append(current)
        current = previous[current]

    path = path[::-1]

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
start = input("Enter start town: ")
destination = input("Enter destination town: ")

# Get both routes
distance_path, total_distance = dijkstra(start, destination, "distance")
time_path, total_time = dijkstra(start, destination, "time")

# Get the missing stat for each path
distance_path_time = path_stats(distance_path, "time")
time_path_distance = path_stats(time_path, "distance")

# Calculate total cost for each route
cost_of_distance_route = total_cost(total_distance, distance_path_time)
cost_of_time_route = total_cost(time_path_distance, total_time)

# Print shortest distance route
route    = " -> ".join(distance_path)
distance = str(total_distance) + " km"
time     = str(distance_path_time) + " minutes"
fuel     = "GHS " + str(round(fuel_cost(total_distance), 2))
cost     = "GHS " + str(round(cost_of_distance_route, 2))

print("\n=== Route for shortest distance ===")
print("Route:     ", route)
print("Distance:  ", distance)
print("Time:      ", time)
print("Fuel Cost: ", fuel)
print("Total Cost:", cost)

# Print fastest time route
route2    = " -> ".join(time_path)
distance2 = str(time_path_distance) + " km"
time2     = str(total_time) + " minutes"
fuel2     = "GHS " + str(round(fuel_cost(time_path_distance), 2))
cost2     = "GHS " + str(round(cost_of_time_route, 2))

print("\n=== Fastest Time Route ===")
print("Route:     ", route2)
print("Distance:  ", distance2)
print("Time:      ", time2)
print("Fuel Cost: ", fuel2)
print("Total Cost:", cost2)

# Compare and recommend
print("\n=== Recommendation System ===")

if cost_of_distance_route < cost_of_time_route:
    cheaper = round(cost_of_distance_route, 2)
    pricier = round(cost_of_time_route, 2)
    print("Take the Shortest Distance Route")
    print("It costs GHS", cheaper, "which is cheaper than GHS", pricier)

elif cost_of_time_route < cost_of_distance_route:
    cheaper = round(cost_of_time_route, 2)
    pricier = round(cost_of_distance_route, 2)
    print("Take the Fastest Time Route")
    print("It costs GHS", cheaper, "which is cheaper than GHS", pricier)

else:
    same = round(cost_of_distance_route, 2)
    print("Both routes cost the same at GHS", same)
    print("Recommendation is to take the Fastest Time Route to save time")