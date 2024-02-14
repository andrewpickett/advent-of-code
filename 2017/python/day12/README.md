# Approach
### Data format

Pretty much this entire puzzle hinged on just setting up the data correctly. I decided to start with just creating
a dictionary mapping a node to all of the immediately connected nodes...pretty much exactly how the input is laid out.

I solved part one by just using only my `0` node and finding all connected children. It worked and it was fast, but
then when part 2 came about, I needed to do the same thing for all nodes. So I moved the logic into my `get_data` method
to initialize like I was doing originally and then for each element in the dictionary, just build out all connected
nodes for all of them. I did this using a BFS-type implementation (keep a queue of elements and traverse down the
tree, adding them until I hit the bottom).

When all is said and done, I had a dictionary with each node and every node they are connected to, directly or indirectly.

### Part 1
> _How many programs are in the group that contains program ID 0?_

With my input data stored as described above, I just had to return the length of the set for my `0` element in my dictionary.

### Part 2
> _How many groups are there in total?_

So by definition, any elements in a group will have the same elements in each of their groups. Meaning, two elements will
have exactly the same group of connected nodes ONLY if they are in the same group. This means I can just compare all of the
groups for each element and store all "different" ones. The easiest way I thought to do this was to just sort the elements
in each group, join them as a string and store them in a set.

Once I iterate through all of the elements/groups, I am left with a set of groups...so just return the length of that set.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |              17 |
