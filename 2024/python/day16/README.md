# Approach
### Data format

Read the input as a `Grid`.

### Part 1
> __

Dijkstra. Just run it to get lowest cost to every node in the grid. Then just grab the value for the End node.

### Part 2
> __

Now that we have the full path with every node's least cost, we can backtrack from the end back to the start to determine
which nodes are on a best path.

TODO: Write a bit more detail here.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             157 |
| **Part Two** |             306 |
