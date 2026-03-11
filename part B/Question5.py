
#Imports heap queue or priority queue algorithm
import heapq

#Creates an empty dictionary called graph
graph = {}

#Open the text file "ghana_cities_graph_2026.txt"
with open("ghana_cities_graph_2026.txt", "r") as file:
    #loops through each line in  the text file
    for line in file:
        
        #Split each line at a comma and 4 pieces
        parts = line.split(",")
        source = parts[0].strip()
        destination = parts[1].strip()
        distance = int(parts[2].strip())
        time = int(parts[3].strip())

        #Creates a space for each town if it does not exist yet
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []

        #Appends the distance, time and neighbour to the space
        graph[source].append((destination, distance, time))
        graph[destination].append((source, distance, time))

#Defines a function called dijkstra with parameters: graph, start, and destination
def dijkstra(graph, start, destinatn):
    
    #Creates an empty dictionary called distance
    distances = {}

    #Checks for each town in the graph
    for town in graph:
        
        #Set all the distances of the town to infinity except for the begining town which is 0
        distances[town] = float('inf')
    distances[start] = 0

    #Creates our list with the begining town at distance 0
    queue = [(0, start)]

    #Creates a tracker which records how we got to each town. None begins with because we have not set off yet
    previous = {town: None for town in graph}

    #Starts a loop
    while queue:
        
        #Picks the closest town from the queue
        current_distance, current_town = heapq.heappop(queue)

        #If we get to the town with the shortest distance , terminate the loop
        if current_town == destination:
            break
        
        #Checks the neighbour of the current town
        for neighbor, distance, time in graph[current_town]:
            
            #Calculates how far to reach the current town
            new_distance = current_distance + distance

            #If the new distance is shorter than what we initially knew, record it to the tracker and add it to the list

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_town
                heapq.heappush(queue, (new_distance, neighbor))

    # Trace back the path from the destination to the begining, then it reverses so it reades start to destination; start -> destination
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    # Print results ← all inside the function now
    print("Shortest Distance Path")
    print("Route:", " -> ".join(path))
    print("Total distance:", distances[destination], "km")

# calls the function
dijkstra(graph, "Accra", "Tamale")

#Defines a new function called dijkstra_time with the parameters: graph, start, destination
def dijkstra_time(graph, start, destination):
    
    #Creates an empty dictionary called times and sets all travel times to infinity except the begining town
    times = {}
    for town in graph:
        times[town] = float('inf')
    times[start] = 0

    #Creates a list with the begining town at time 0
    queue = [(0, start)]

    #creates a tracker and records how we get to each town
    previous = {town: None for town in graph}

    #Be in a loop as long as there are towns to travel to
    while queue:
        
        #Picks the fastst town from the queue with the smallest travel time
        current_time, current_town = heapq.heappop(queue)

        #If we get to our current destination, terminate the loop
        if current_town == destination:
            break
        
        #Checks the neighbour of the current town
        for neighbor, distance, time in graph[current_town]:
            new_time = current_time + time   # ← time not distance

            if new_time < times[neighbor]:
                
                times[neighbor] = new_time
                previous[neighbor] = current_town
                heapq.heappush(queue, (new_time, neighbor))

    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    print("Fastest Time Path")
    print("Route:", " -> ".join(path))
    print("Total time:", times[destination], "minutes")


dijkstra_time(graph, "Accra", "Tamale")