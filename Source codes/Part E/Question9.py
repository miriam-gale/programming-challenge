# Question9
import heapq

#Assumed constants
FUEL_CONSUMPTION = 8
FUEL_PRICE = 11.95
TIME_COST = 0.5

# Created an empty dictionary called graph
graph = {}

#Opens the text file "ghana_cities_graph_2026.txt"
with open("ghana_cities_graph_2026.txt","r") as file:

  #for each line in a file
  for line in file:

    #Split a line at each comma into 4 pieces
    parts = line.split(",")
    source = parts[0].strip()
    destination = parts[1].strip()
    distance = int(parts[2].strip())
    time = int(parts[3].strip())

    #Creates an empty list if source and destination is not found in the graph
    if source not in graph:
      graph[source] = []
    if destination not in graph:
      graph[destination] = []



    # Appends it to the list if any
    graph[source].append((destination, distance, time))
    graph[destination].append((source, distance, time))

def dijkstra(graph, start, destination):
    
    # Creates an empty dictionary called distance
    distances = {}

    # Checks for each town in the graph
    for town in graph:
        
        # Set all the distances of the town to infinity except for the begining town which is 0
        distances[town] = float('inf')
    distances[start] = 0

    # Creates our list with the begining town at distance 0
    queue = [(0, start)]

    # Creates a tracker which records how we got to each town. None begins with because we have not set off yet
    previous = {town: None for town in graph}

    # Starts a loop
    while queue:
        
        # Picks the closest town from the queue
        current_distance, current_town = heapq.heappop(queue)

        # If we get to the town with the shortest distance , terminate the loop
        if current_town == destination:
            break
        
        # Checks the neighbour of the current town
        for neighbor, distance, time in graph[current_town]:
             
            # Calculates how far to reach the current town
            new_distance = current_distance + distance

            # If the new distance is shorter than what we initially knew, record it to the tracker and add it to the list

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_town
                heapq.heappush(queue, (new_distance, neighbor))
    
    #Tracks the path
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path, distances[destination]


def dijkstra_time(graph, start, destination):
    
    # Creates an empty dictionary called times and sets all travel times to infinity except the begining town
    times = {}
    for town in graph:
        times[town] = float('inf')
    times[start] = 0

    # Creates a list with the begining town at time 0
    queue = [(0, start)]

    # creates a tracker and records how we get to each town
    previous = {town: None for town in graph}

    # Be in a loop as long as there are towns to travel to
    while queue:
        
        # Picks the fastst town from the queue with the smallest travel time
        current_time, current_town = heapq.heappop(queue)

        # If we get to our current destination, terminate the loop
        if current_town == destination:
            break
        
        # Checks the neighbour of the current town
        for neighbor, distance, time in graph[current_town]:
            new_time = current_time + time   # ← time not distance

            if new_time < times[neighbor]:
                
                times[neighbor] = new_time
                previous[neighbor] = current_town
                heapq.heappush(queue, (new_time, neighbor))

    path = []
    current = destination

    while current != None:
        path.append(current)
        current = previous[current]

    path = path[::-1]

    return path, times[destination]



def path_stats(path, stat):
    total = 0
    for i in range(len(path) - 1):
        town_a = path[i]
        town_b = path[i + 1]
        for neighbor, dist, time in graph[town_a]:
            if neighbor == town_b:
                if stat == "distance":
                    total += dist
                else:
                    total += time
                break
    return total




    

#Creates an interactive loop
while True:
    #Displays the options to the user
    print("\n===== Ghana Transport System =====")
    print("1. Find routes between towns")
    print("2. Update the road network")
    print("3. Quit")
    
    # Prompts the user to enter a choice
    user_input = input("Enter your choice: ")

    # Checks if the user input is 1, if 1
    if user_input == "1":


        #Ask which town the user is starting from
        begining_town = input("What is your begining town?: ")
        #Ask which town the user is heading to
        destination_town = input("What is your destination town?: ")

        if begining_town not in graph or destination_town not in graph:
            print("One or both towns not found! Try again")
        else:
            #Calls the dijkstra function
            path, dist = dijkstra(graph, begining_town, destination_town)
            time_path, total_time = dijkstra_time(graph, begining_town, destination_town)

            dist_path_time = path_stats(path, "time")
            time_path_dist = path_stats(time_path, "distance")

            # Calculates the fuel cost of the distance
            dist_fuel_cost = (dist / FUEL_CONSUMPTION) * FUEL_PRICE

            #Calculates the total cost
            dist_total_cost = dist_fuel_cost + (dist_path_time * TIME_COST)
            
            # Calculates the time fuel cost
            time_fuel_cost = (time_path_dist / FUEL_CONSUMPTION) * FUEL_PRICE
            time_total_cost = time_fuel_cost + (total_time * TIME_COST)

            #Prints the Shortest distance
            print("\nShortest Distance Path")

            #Prints the route
            print("Route:", " -> ".join(path))

            #Prints the distance in kilometers
            print("Distance:", dist, "km")

            #Prints the time in minutes
            print("Time:", dist_path_time, "minutes")
            
            #Prints the fastest time path
            print("\nFastest Time Path:")

            #Prints the route
            print("Route:", " -> ".join(time_path))

            #Prints the distance in kilometers
            print("Distance:", time_path_dist, "km")

            #Prints the time in minutes
            print("Time:", total_time, "minutes")
            
            #Prints the cost comparison
            print("\nCost Comparison:")

            # Prints the shortest route in Ghana Cedis and round the cost to 2 decimal points
            print("Shortest Distance Route: GHS", round(dist_total_cost, 2))

            #Prints the fastest time route and round the total cost in Ghana Cedis to 2 decimal points
            print("Fastest Time Route: GHS", round(time_total_cost, 2))
        
            #Prints the recommendation
            print("\n=== Recommendation ===")

            #Checks if the total distance cost is less than the time total cost
            if dist_total_cost < time_total_cost:
                # And prints "Take the shortest distance route"
                print("Take the shortest distance route!")

                #Also prints it costs the total distance cost in 2 decimal points
                print("It costs GHS", round(dist_total_cost, 2), "which is cheaper!")

                #Else if that condition is not fulfilled it checks if the time total cost is less than the distance total cost
            elif time_total_cost < dist_total_cost:
                # And prints "Take the fastest time route"
                print("Take the fastest time route!")

                # Also prints it costs time total cost to 2 decimal points
                print("It costs GHS", round(time_total_cost, 2), "which is cheaper!")

            #Else if that condition is not fulfilled
            else:
                #It prints "Both routes cost the amount " to 2 decimal points
                print("Both routes cost the same at GHS", round(dist_total_cost, 2))

                #Prints the recommendation: To take the fastest time time route to save time
                print("Recommendation: Take the Fastest Time Route to save time!")
        
    # If the user choose to enter "2":
    elif user_input == "2":

        #Prints "Update Road Network"
        print("\n===Update Road Network ===")

        #Prints the options
        print("a. Change travel time")
        print("b. Remove a road")
        print("c. Add a new road")
        
        #Prompts the user to enter an option
        update_choice = input("Enter preferrable choice: ")
        
        #Check if the user's choice is "a", if "a"
        if update_choice == "a":

            #Prompts the user to enter the name of the first town
            town_a = input("Enter the first town: ")

            #Prompts the user to enter the name of the second town
            town_b = input("Enter second town: ")

            #Prompts the user to enter the new travel time between these two towns in minutes
            new_travel_time = int(input("Enter new travel time(minutes): "))

            # Update the time in both directions
            graph[town_a] = [(n, d, new_travel_time) if n == town_b else (n, d, t) for n, d, t in graph[town_a]]

            graph[town_b] = [(n, d, new_travel_time) if n == town_a else (n, d, t) for n, d, t in graph[town_b]]
            print("Travel time updated successfully!")

        elif update_choice == "b":
            #Prompts the user to enter the first town
            town_a = input("Enter first town: ")

            #Prompts the user to enter the second town
            town_b = input("Enter second town: ")

            #Remove in both directions
            graph[town_a] = [(n, d, t) for n, d, t in graph[town_a] if n != town_b]

            graph[town_b] = [(n, d, t) for n, d, t in graph[town_b] if n != town_a]
            
            #Prints "Road removed successfully!"
            print("Road removed successfully!")
        
        #Checks if the option is "c"
        elif update_choice == "c":
            #Prompts the user to enter the first town
            town_a = input("Enter first town: ")

            #Prompts the user to enter the second town
            town_b = input("Enter second town: ")
            
            #Prompts the user to enter a new distance
            new_distance = int(input("Enter distance (km): "))
            
            #Prompts the user to enter a new time
            new_time = int(input("Enter travel time(minutes): "))

            #Add road in both directions
            graph[town_a].append((town_b, new_distance, new_time))

            graph[town_b].append((town_a, new_distance, new_time))

            #Prints "Road added successfully"
            print("Road added successfully!")

    elif user_input == "3":
        print("Goodbye")
        break
    else: 
        print("Invalid choice")