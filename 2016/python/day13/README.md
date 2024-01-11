# Approach
### Data format

I read in the input file as the integer that it is. I then take that number and build a Grid (using my `Grid` class)
and set the value of each `Point` based on the formula in the puzzle. At the end, I have a Grid and a target
location that I'm trying to reach.

### Part 1
> _What is the fewest number of steps required for you to reach 31,39?_

Ugh...Maze traversal. I hate doing these, because typically even just creating the grid in a logical data structure (2d array)
is a pain, and then actually doing the traversal is always tricky. Luckily this one wasn't asking anything too complicated
and a simple breadth-first-search would be good enough.

I also had already written my own "Grid" class that I was able to just extend to include an optional "visited" field on each Point.

So, in the end, I was able to just instantiate a new Grid, set the values of the Points based on the formula outlined,
and then I had my office maze completely initialized.

I then implemented a basic BFS, where you just add valid neighbors to a queue with an increased value of "1" and keep
dequeueing items until the queue is empty or you reach the target node. Ended up working pretty well.

### Part 2
> _How many locations (distinct x,y coordinates, including your starting location) can you reach in at most 50 steps?_

For this one, I just modified my BFS to just count the number of nodes visited and I don't add any that have a value of 50 or more.
This forces my queue to empty out quicker, and I hit every space that can be hit within 50 away from the start. I made a mistake at first
by including a distance of 51, which gave me an answer too high...so a quick fix and everything was good.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               7 |
| **Part Two** |              <1 |
