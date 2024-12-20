# Approach
### Data format

Read the input as a `Grid`, and then also include the minimum savings I care about counting. This will help with unit
testing.

### Part 1
> _How many cheats would save you at least 100 picoseconds?_

Dijkstra, Dijkstra, Dijkstra...again!

Basically I run Dijkstra on the grid to find the shortest path from start to finish. Then, I ORIGINALLY just went through
and systematically removed each wall, one at a time and re-ran Dijkstra on the new grid and subtracted the new best distance
from the original. Any that were 100 better or more, I counted. Worked great on the example...and it worked on my input
as well, but it took almost 25 minutes to run.

So while it was running, I started trying to think of a better way. I ended up realizing, a "shortcut" is simply taking
any two points on the current best path, and removing a wall between them. This ends up meaning the "savings" is the
distance between those 2 points on the best path minus the Manhattan distance between the two points (which in this case
is always 2).

So I quickly changed my algorithm to still do the original Dijkstra, and then just go through every single pair of points
along the path and if they are within 2 distance of each other, simply subtract the index of where they are in the original path
and their distance away from each other...giving the savings between them. Now this isn't the most efficient, because I'm doing
that for EVERY PAIR of points. In the case where there is no wall between the two points, it's not going to save any time.

But it runs in about 15 seconds...which is MUCH better than 25 minutes, so it's good enough for me for now.

### Part 2
> _How many cheats would save you at least 100 picoseconds?_

Literally I just have to change my algorithm to check any two points on the path where the Manhattan distance is less than or equal
to 20 now, instead of just 2! It's going to be literally the exact same code.

So, by the time I finished re-coding my algorithm for part 1, part 2 was also complete.

Also takes about 15 seconds, so again, I know I can optimize, but it's fine for now...and I can go to bed.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |           15569 |
| **Part Two** |           16093 |
