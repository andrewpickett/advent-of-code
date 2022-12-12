# Approach
### Part 1
> _What is the fewest steps required to move from your current position to the location that should get the best signal?_

BFS for the win!

So, I immediately recognized this as a problem that could easily be solved by breadth-first-search. I quickly wrote up
a BFS algorithm utilizing the Grid utility I wrote in previous AoC events. I thought I had it all right, and ran it against the example,
but my answer was wrong. I ended up spending about 10 minutes debugging only to find I forgot to include the end point, `E`,
in my list of valid points -- which means it was returning a value of `-1`, which always passed the check on if we can move
from one space to the next. This means the first time my traversal made it as a neighbor to `E` it was ending...

Once I added the end point to my list, it worked perfectly.

### Part 2
> _What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?_

Well, let's just run it a bunch of times! Basically loop over the input to find all spaces that are either `S` or `a` and
add them to a list. Then run my BFS algorithm with each start point and take the minimum. I did it, ran it, and got the wrong
answer. Turns out I wasn't "resetting" my grid after each run, so when it ran the second starting point, all of the nodes
had been visited already -- so just a quick reset after each run, and it worked great.

Love it when things work out as well as this!

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |    352 |        1 |             140 |              00:25:58 | 1664 |
| **Part Two** |    345 |        2 |            2588 |              00:08:39 | 1883 |

# Original puzzle
### --- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from
above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where `a` is
the lowest elevation, `b` is the next-lowest, and so on up to the highest elevation, `z`.

Also included on the heightmap are marks for your current position (`S`) and the location that should get the best signal (`E`).
Your current position (`S`) has elevation `a`, and the location that should get the best signal (`E`) has elevation `z`.

You'd like to reach `E`, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up,
down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than
the elevation of your current square; that is, if your current elevation is `m`, you could step to elevation `n`, but not to elevation `o`.
(This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

```
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
```

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need
to head toward the `e` at the bottom. From there, you can spiral around to the goal:

```
v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
```

In the above diagram, the symbols indicate whether the path exits each square moving up (`^`), down (`v`), left (`<`), or right (`>`).
The location that should get the best signal is still `E`, and `.` marks unvisited squares.

This path reaches the goal in `31` steps, the fewest possible.

### --- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic,
though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation `a`. The goal is still the square marked `E`.
However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from
any square at elevation `a` to the square marked `E`.

Again consider the example from above:

```
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
```

Now, there are six choices for starting position (five marked `a`, plus the square marked `S` that counts as being at elevation `a`).
If you start at the bottom-left square, you can reach the goal most quickly:

```
...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
```

This path reaches the goal in only `29` steps, the fewest possible.
