# Approach
### Data format

I decided to build a tree as part of the input. Basically create a map of the location as the key, and a `TreeNode` as
the value. If there is already a `TreeNode` with that key, then append the location as a child.

### Part 1
> _What is the total number of direct and indirect orbits in your map data?_

Now that I have a full tree, it's pretty simple to just loop over every single node, get the tree from it, and count
how long that specific branch is. I do that for every single node/point. This will by nature count all of them (even the
subtrees) because every node has a full chain back to the root to count.

Add them all up, and we're done.

### Part 2
> _What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting?_

At its core, all this part of the puzzle is is to find the distance between the two nodes and their first common
ancestor. So I just start with the `YOU` node and start traversing up the tree. At each point, check if that node is
in the tree for `SAN`. Once we find one, we know that is the first common ancestor...which means we just need to count
how far up the tree it is from both of the nodes and add it together. Since I have the ancestry stored as a list in both
nodes, I can just get the indexes of that ancestor in both chains and add them together.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
