# Approach
### Data format

Ah, the first puzzle where reading the input into an appropriate data structure is essential! For this I decided to actually
just build a tree. So to do this, I just created a simple `Node` class that keeps track of its parent, children, and its own weight.
It also has the ability to store the weight of all of its children (used in part 2). So really in the end, it's just a single
node (the root) and a bunch of nodes connected to each other.

Since it's all kept track in just references in objects, I store all of the nodes individually in a map for easy lookup later.

### Part 1
> _What is the name of the bottom program?_

Really this is just asking for the root node. Since I've already built the tree, it's just the first node in the list that
doesn't have a parent.

### Part 2
> _Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?_

Alright, so the first step I did was to calculate the entire tower weight for each node. I do this recursively by starting
at the root and just adding the weights of all the child towers. If a node has no children, then the tower weight is just its
own weight.

Now that I have all of the tower weights, I start traversing through the tree, checking each level's node's tower weights.
Once I find a level that has an imbalance, I just need to figure out which one needs adjusted and by how much. I traverse through
that specific tower until I reach a place where they are balanced again. At that point, I know how much it needs to be adjusted
so I just return that value.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
