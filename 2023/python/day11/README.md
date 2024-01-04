# Approach
### Part 1
> _What is the sum of these lengths?_

I first wrote this by actually adding the rows that needed to be added by appending them to the array as I parsed the
input. The columns were a little tricker, but I did that by rotating the 2d array and then checking them as rows and appending
any new rows I needed. I then rotated it back to have my newly expanded universe.

Awesome.

The rest was really simple, because in all of his talk about how to calculate distance between pairs of galaxies, it all
was just using Manhattan Distances. So I looped through every galaxy in the `Grid` and just did a simple distance calculation
on it:
```
|d1[x] - d2[x]| + |d1[y] - d2[y]|
```
Pretty simple and it gave me the correct answer.

### Part 2
> _What is the sum of these lengths?_

Yep, I figured something like this would happen...but I was expecting much worse (like the galaxy is CONSTANTLY expanding) or something...
so I was happy to see it was just a static increase.

Obviously I'm not going to be able to use my initial strategy in actually appending the rows/cols to the data grid in this scenario.

It was pretty clear to me, though, that since we're just using Manhattan Distances for all of the measurements, every expansion
would just increase the distance it by that amount.

So really you just need to know how many rows/columns that would be expanded you cross when going between 2 galaxies. Once you know how many
you cross, you just multiply that by the scale and add it to your original distance.

Really didn't take long to rewrite my part 1 to use this and test it and then just run it on part 2. Done.

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------:|----------------:|----------------------:|-----:|
| **Part One** |        1 |             590 |              00:41:12 | 5312 |
| **Part Two** |        1 |             589 |              00:56:36 | 4899 |


# Original puzzle
### --- Day 11: Cosmic Expansion ---
You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within turns out to be a researcher studying cosmic expansion using the giant telescope here.

He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once he's done with today's observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a single giant **image** (your puzzle input). The image includes **empty space** (`.`) and **galaxies** (`#`). For example:
```
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
```
The researcher is trying to figure out the sum of the lengths of the **shortest path between every pair of galaxies**. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.

Due to something involving gravitational effects, **only some space expands**. In fact, the result is that **any rows or columns that contain no galaxies** should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:
```
   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
```
These rows and columns need to be **twice as big**; the result of cosmic expansion therefore looks like this:
```
....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......
```
Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:
```
....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......
```
In these 9 galaxies, there are **36 pairs**. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one `.` or `#` at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies `5` and `9`:
```
....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......
```
This path has length **`9`** because it takes a minimum of nine steps to get from galaxy `5` to galaxy `9` (the eight locations marked `#` plus the step onto galaxy `9` itself). Here are some other example shortest path lengths:

- Between galaxy `1` and galaxy `7`: 15
- Between galaxy `3` and galaxy `6`: 17
- Between galaxy `8` and galaxy `9`: 5

In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is **`374`**.

Expand the universe, then find the length of the shortest path between every pair of galaxies. **What is the sum of these lengths**?

### --- Part Two ---
The galaxies are much **older** (and thus much **farther apart**) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column **one million times** larger. That is, each empty row should be replaced with `1000000` empty rows, and each empty column should be replaced with `1000000` empty columns.

(In the example above, if each empty row or column were merely `10` times larger, the sum of the shortest paths between every pair of galaxies would be **`1030`**. If each empty row or column were merely `100` times larger, the sum of the shortest paths between every pair of galaxies would be **`8410`**. However, your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. **What is the sum of these lengths**?