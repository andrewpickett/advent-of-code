# Approach
### Data format

Read both wire directions as a list of directions. That's it.

### Part 1
> _What is the Manhattan distance from the central port to the closest intersection?_

I decided to just literally traverse the entire wire, storing each point it hits as we travel. All I need to do is
keep track of the current position. Since I'm literally walking the wire one space at a time, I can just use my `DIRS`
utility map and add that to my current direction over and over for each step to "traverse" the wire.

At the end, I have 2 arrays containing all positions of the wires. In order to find the closest intersection, I convert
them to sets, use the set `intersection` functionality to find all times the wires cross each other, and then just
loop through them to find the minimum manhattan distance.

### Part 2
> _What is the fewest combined steps the wires must take to reach an intersection?_

Since I already have the two wires, and I have their traversal IN ORDER, I can again use the intersection functionality
of the set to find all crossing points and then just lookup the index on both wires of those intersections. The minimum
is the one I care about. I do have to add `2` to the total, because it needs to count the origin, but I don't have those
in my lists (since then the minimum would always be the origin itself). So adding `2` to the total here counts the origin
in both wires.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             297 |
| **Part Two** |             309 |
