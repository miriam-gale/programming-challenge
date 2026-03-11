#Creates an empty set called towns
towns = set()

#Creates a counter called edges starting from zero. 
edges = 0


# Opens the text file "ghana_cities_graph_2026.txt"
with open("ghana_cities_graph_2026.txt", "r") as file:

  #Goes through every line in our text file
  for line in file:

    #At each comma in a line, the line is splitted
    parts = line.split(",")

    #Grabs the first and second pieces and removes the extra spaces
    source = parts[0].strip()
    destination = parts[1].strip()

    #Adds both towns to our set created
    towns.add(source)
    towns.add(destination)

    #Adds 2 to our counter because each line is 2 roads
    edges = edges + 2

    #prints the final counts
  print("Total towns:", len(towns))
  print("Total roads:", edges)


