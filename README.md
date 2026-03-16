# Ghana Cities Graph Programming Challenge

This project analyzes a network of Ghanaian cities and roads using Python. It demonstrates how to read a graph from a file, construct data structures, and solve real-world routing problems such as finding shortest paths, fastest routes, and calculating travel costs.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [File Format](#file-format)
- [Questions Answered](#questions-answered)
- [Requirements](#requirements)

---

## Overview

The program reads a file describing roads between towns in Ghana, builds a graph, and answers questions about routes, distances, times, and costs using algorithms like Dijkstra's.

---

## Features

- Counts total towns and roads.
- Builds a graph from a text file.
- Finds neighbors of a town.
- Computes shortest and fastest routes using Dijkstra's algorithm.
- Lists top 3 shortest paths between towns.
- Calculates fuel and total travel costs.
- Recommends the most cost-effective route.

---

## How It Works

1. **Reads Data:** Loads city and road data from `ghana_cities_graph_2026.txt`.
2. **Builds Graph:** Stores towns and roads in a dictionary.
3. **Pathfinding:** Uses Dijkstra's algorithm for shortest and fastest routes.
4. **Cost Calculation:** Computes fuel and total costs based on distance, time, and fuel price.
5. **Recommendation:** Compares routes and suggests the cheaper option.

---

## Usage

1. Place `ghana_cities_graph_2026.txt` in the same directory as the script.
2. Run the script with Python 3.
3. Follow prompts to enter start and destination towns.
4. View results for routes, distances, times, costs, and recommendations.

---

## File Format

Each line in `ghana_cities_graph_2026.txt` should be:

```
SourceTown, DestinationTown, DistanceInKm, TimeInMinutes
```

Example:

```
Accra, Kumasi, 250, 240
```

---

## Questions Answered

1. **Count towns and roads:** Reads the file and counts unique towns and total roads.
2. **Construct the graph:** Builds a dictionary mapping each town to its neighbors.
3. **Find neighbors:** Returns all directly connected towns for a given town.
4. **Shortest/fastest route:** Uses Dijkstra's algorithm for both distance and time.
5. **Top 3 shortest paths:** Finds alternative shortest routes by temporarily removing roads.
6. **Fuel cost:** Calculates cost based on distance, fuel consumption, and price.
7. **Total cost & recommendation:** Adds time cost to fuel cost and recommends the cheaper route.

---

## Requirements

- Python 3.x
- `ghana_cities_graph_2026.txt` data file

---

## Notes

- Ensure the data file is correctly formatted.
- The code uses standard Python libraries only.

---

**Author:** _Your Name Here_
