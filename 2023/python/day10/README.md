# Approach
### Part 1
> _How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?_

First go at it, I immediately used my `Grid` utility to parse the data into a grid where I can get neighbors and everything.
So far so good. The first step was to find the start position and identify what actual pipe type it was. I did that by
finding the `S`, checking all of the neighbors and determining which neighbors "connect" to that node. From there you can
determine the ACTUAL type of pipe that `S` is.

Next you need to determine from which direction you "entered" that position. Basically which direction are you going to travel
along the path. I just arbitrarily picked one to start, because it shouldn't matter in the long run...

Now, I just went ahead and followed the path. The way I do this is moving along the grid using my neighbor helpers based on the
direction I came from and the current pipe type. For example, if I am on an `F`, and I came from the south (`S`), the next
node would be my east neighbor.

As I visit each node along the path, I add it to a set to keep track of the entire path. Once I find a value already in the
set, I know I'm back to the start, so I have the full path.

The distance that we care about is the one that's the farthest away -- which will always be half the length of the path,
so that part's easy to calculate. Done with part 1.

**NOTE** I went back after completing part 2 to work on optimizing a little bit, as part 2 took over 10 minutes to run.
I followed the same logic, but just stopped using my `Grid` utility, as the lookups for the neighbors were expensive and
unnecessary. As part of converting this to native arrays, I also pad the entire perimeter with an additional row/column of
`.` to avoid having to check "edges" constantly.

### Part 2
> _How many tiles are enclosed by the loop?_

Oof, this one was not as easy as I thought it would be -- but also just as simple...

My first thought with this was to just do a simple flood fill algorithm to find all the "interior" points. I wrote it up,
I KNOW it was right and it looked good...but I was getting the wrong answer. I then realized because of how the pipes are
on the grid, there are times you can't get "between" them to get out. For example a grid with `||` should allow the flood
to pass through them, but since there's no actual POINT between those two, the algorithm can't find it.

So...I started re-thinking this. I really had 2 options:
1) I could in theory double the size of the input, and pad everything so that there WOULD be space between those types of pipes, but the thought of how to do that easily (especially since I was using my `Grid` class) was quite overwhelming at 1:00am.
2) Use the Even-Odd rule to determine if something is in or out.

I decided to go with the Even-Odd, as it seemed like it would be much simpler to implement. **Side note**: I actually didn't know
"Even-Odd" rule was an actual RULE and well documented until after I wrote this. The concept just made sense, and while I was
writing it I looked it up and sure enough it had an official name!

Basically, for any given point, you can just count the number of times you cross a wall (aka a pipe along the path) from the left
before getting to your point. If the number of times you cross is odd, then you are INSIDE the path. Otherwise, you're OUTSIDE.

So the use cases you need to account for here are:
- `|` -- One of these along the path is clearly a wall, and so that counts as a crossing
- `FJ` -- any time you have an `FJ` combination, with any number of `-` between them, it counts as a single crossing
- `L7` -- similarly, this combination with any number of `-` between them, also counts as a single crossing.

So I got to work implementing this (still using my `Grid` class). There were a couple little edge cases that tripped me up for a few
minutes, but overall, it was pretty clean.

I ran the code...and it ran...and ran...and ran...I was tired, I didn't want to rewrite this thing again...it still ran...

Finally, after over 10 minutes, it gave me an answer. I plugged it in and to my amazement, it was correct!! I got a top 1000
finish for it, but it was UGLY!!!

I decided later to go back and optimize it a little bit, which mainly consisted of removing my `Grid` completely and just
treating it as a native 2d array. This brought it down to about 5 seconds (with 2 of those seconds just building the path like in part 1).

Overall, it could be much better, but I'm happy with for now.

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------:|----------------:|----------------------:|-----:|
| **Part One** |        1 |            1975 |              00:48:14 | 3159 |
| **Part Two** |        3 |            5463 |              01:06:21 |  836 |


# Original puzzle
### --- Day 10: Pipe Maze ---
You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.

You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.

Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of **tiles**:

- `|` is a **vertical pipe** connecting north and south.
- `-` is a **horizontal pipe** connecting east and west.
- `L` is a **90-degree bend** connecting north and east.
- `J` is a **90-degree bend** connecting north and west.
- `7` is a **90-degree bend** connecting south and west.
- `F` is a **90-degree bend** connecting south and east.
- `.` is **ground**; there is no pipe in this tile.
- `S` is the **starting position** of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is **one large, continuous loop**.

For example, here is a square loop of pipe:
```
.....
.F-7.
.|.|.
.L-J.
.....
```
If the animal had entered this loop in the northwest corner, the sketch would instead look like this:
```
.....
.S-7.
.|.|.
.L-J.
.....
```
In the above diagram, the `S` tile is still a 90-degree `F` bend: you can tell because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that **aren't connected to the loop**! This sketch shows the same loop as above:
```
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
```
In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to `S`, pipes those pipes connect to, pipes **those** pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including `S`, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:
```
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
```
Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:
```
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
```
If you want to **get out ahead of the animal**, you should find the tile in the loop that is **farthest** from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps **along the loop** to reach from the starting point - regardless of which way around the loop the animal went.

In the first example with the square loop:
```
.....
.S-7.
.|.|.
.L-J.
.....
```
You can count the distance each tile in the loop is from the starting point like this:
```
.....
.012.
.1.3.
.234.
.....
```
In this example, the farthest point from the start is **`4`** steps away.

Here's the more complex loop again:
```
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
```
Here are the distances for each tile on that loop:
```
..45.
.236.
01.78
14567
23...
```
Find the single giant loop starting at `S`. **How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?**

### --- Part Two ---
You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is **within the area enclosed by the loop**?

To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:
```
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
```
The above loop encloses merely **four tiles** - the two pairs of `.` in the southwest and southeast (marked `I` below). The middle `.` tiles (marked `O` below) are **not** in the loop. Here is the same loop again with those regions marked:
```
...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....
```
In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, `I` is still within the loop and `O` is still outside the loop:
```
..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
```
In both of the above examples, **`4`** tiles are enclosed by the loop.

Here's a larger example:
```
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
```
The above sketch has many random bits of ground, some of which are in the loop (`I`) and some of which are outside it (`O`):
```
OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
```
In this larger example, **`8`** tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:
```
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
```
Here are just the tiles that are **enclosed by the loop** marked with `I`:
```
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
```
In this last example, **`10`** tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the area within the loop. **How many tiles are enclosed by the loop**?
