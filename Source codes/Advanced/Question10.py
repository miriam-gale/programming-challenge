# Question 10 - Time Complexity Analysis
#Imports mathplotlib
import matplotlib.pyplot as plt

#import math
import math

# Number of towns (V)
towns = [100, 200, 500, 1000, 2000, 3000, 4000, 5000]

# Steps = V * log2(V) for Dijkstra with heapq
steps = [v * math.log2(v) for v in towns]

# Mark our actual dataset
actual_towns = 183
actual_steps = actual_towns * math.log2(actual_towns)

# Plot the main line
plt.plot(towns, steps, color="blue", marker="o", label="Dijkstra O(V log V)")

# Mark our actual dataset with a red dot
plt.plot(actual_towns, actual_steps, color="red", marker="*", 
         markersize=15, label="Our dataset (183 towns)")

# Labels
#Gives the graph a title
plt.title("Dijkstra's Algorithm - Scalability Analysis\n100 to 5000 towns")
#Labels the x-axis
plt.xlabel("Number of Towns (V)")

#Labels the y-axis
plt.ylabel("Estimated Steps (V log V)")

# Add grid and legend
plt.grid(True)
plt.legend()

# Show values on each point
for v, s in zip(towns, steps):
    plt.annotate(f"{int(s)}", (v, s), textcoords="offset points",  xytext=(0, 10), ha="center", fontsize=8)

# Save the graph as an image
plt.savefig("time_complexity_graph.png")
print("Graph saved as time_complexity_graph.png")

#Show the graph
plt.show()
