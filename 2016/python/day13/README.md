# Approach
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

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |     82 |        1 |              29 |                   N/A |  N/A |
| **Part Two** |    138 |        2 |              39 |                   N/A |  N/A |


# Original puzzle
### --- Day 13: A Maze of Twisty Little Cubicles ---
You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one. Instead, you are in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers (`x,y`). Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at
`0,0` and seems to extend infinitely toward positive `x` and `y`; negative values are invalid, as they represent a location outside the building. You are in a small waiting area at `1,1`.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given x,y coordinate will be a wall or an open space using a simple system:

* Find `x*x + 3*x + 2*x*y + y + y*y`.
* Add the office designer's favorite number (your puzzle input).
* Find the binary representation of that sum; count the number of bits that are `1`.
  * If the number of bits that are `1` is even, it's an open space.
  * If the number of bits that are `1` is odd, it's a wall.

For example, if the office designer's favorite number were `10`, drawing walls as `#` and open spaces as `.`, the corner of the building containing `0,0` would look like this:

```
  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###
```

Now, suppose you wanted to reach `7,4`. The shortest route you could take is marked as `O`:

```
  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###
```

Thus, reaching `7,4` would take a minimum of `11` steps (starting from your current location, `1,1`).

### --- Part Two ---
