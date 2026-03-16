# Question 2 - Constructing the graph

# Creates an empty dictionary called graph
graph = {}

# Open the text file "ghana_cities_graph_2026.txt"
with open("ghana_cities_graph_2026.txt", "r") as file:
  # loops through each line in  the text file
  for line in file:

    # Split each line at a comma and 4 pieces
    parts = line.split(",")
    source = parts[0].strip()
    destination = parts[1].strip()
    distance = int(parts[2].strip())
    time = int(parts[3].strip())

    # Creates a space for each town if it does not exist yet
    if source not in graph:
      graph[source] = []

    if destination not in graph:
      graph[destination] = []

    # Appends the distance, time and neighbour to the space
    graph[source].append((destination, distance, time))

    graph[destination].append((source, distance, time))

# Display the graph
print(graph)


# Defines a function with a parameter town
def get_neighbours(town):

  # Look for the town in the graph dictionary and assign it to neighbours and returns it
  neighbours = graph[town]
  return neighbours

# Calls the function with a specific town "Assin Fosu"
print(get_neighbours("Assin Fosu"))
  