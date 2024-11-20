# Approach
### Data format

I first started by creating the grid using my `Grid` class, since I knew I'd probably be doing some sort of
traversals...and I ended up solving the first part with it, but it took a long time, and I then realized pretty
quickly that part 2 would take forever with it. I took a look and noticed that I don't need to store that much
information in the grid and I can just store the erosion level at each point in the grid and everything else could
be derived from that. So all I initially store in my data is the depth, the target coordinate, and a blank 2d array
that has some extra padding to account for additional traversals later on...those numbers were found by just
running my algorithm until I stopped getting an index out of bounds exception :c)

### Part 1
> _What is the total risk level for the smallest rectangle that includes 0,0 and the target's coordinates?_

We just need to add up all of the erosion levels mod 3 for each square in the grid. So we loop over the `X x Y` sized
rectangle for the target, calculate all of the erosion levels for every square and then sum up the mod 3 of them.

Pretty simple, actually.

### Part 2
> _What is the fewest number of minutes you can take to reach the target?_

Here's where it got more interesting and fun. I noticed pretty quickly that this was going to be a "shortest" path
problem, but the weight was no longer just a simple edge weighting. Instead there were multiple aspects that would
go into determining the weight for each node -- so to me that meant looking at using a priority queue. I spent some time
trying to write my own, because I ALWAYS -- EVERY YEAR WITHOUT FAIL -- forget that Python has a `heapq` already.

So after wasting a bunch of time trying to re-invent the wheel, I ended up just using the `heapq`.

Basically just use the rules described in the problem to add items to the heap and keep track of best times to the target.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              15 |
| **Part Two** |           10156 |
