# Approach
So, I initially wrote this all inline and had a method to check for neighbors and everything. I didn't do anything
with classes or object-oriented at all.

After I got the answer, I decided to refactor it to use some simple "Grid" and "Point" classes just because I foresee
needing to do this sort of thing a lot in future exercises, so I added those classes to my utils package. I created them
in such a way that you can optionally populate every point's neighbors, either orthogonal or diagonal which will help
in the future.

It does assume the data coming in are formatted as an array of arrays, and currently assumes them to all be strings.

It causes this specific puzzle to run slightly slower (e.g. 250ms --> 350ms), but it is much more robust and reusable
and will certainly help out whenever I have this sort of need in the future.

### Part 1
> _What is the sum of the risk levels of all low points on your heightmap?_

More multi-dimensional arrays...woohoo...

I really did just approach this in the most straightforward way I could: read the data into a 2-d array and then iterate
over every entry. For each entry, find all of its neighboring values and if all of them were higher than itself, add it (plus 1)
to my total.

### Part 2
> _What do you get if you multiply together the sizes of the three largest basins?_

RECURSION! YAY! I actually do like recrusive puzzles, so that's how I solved this one. Basically for each of the low
points (found in part 1), we check all of the neighbors. For any of the neighbors that are larger than itself and NOT
a "9", we travel to those points and check their neighbors and continue that until there are no neighbors left that meet
the criteria. All the while, we are keeping track of which points we have already visited so as to not double count them
or include them as neighbors again (as that would cause us to infinitely loop between those 2 points).

In the end, after we have travelled to all of the points that flow down to the basin, we have an array of "visited"
points that we can then use to tell how many points flow down to the basin.

From there, just sort that array and grab the largest 3 and multiply them together.


# Results

|              |  Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|--------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |     458 |        1 |             113 |              00:18:03 | 4186 |
| **Part Two** | 1391940 |        1 |             337 |              00:39:19 | 4704 |

# Original puzzle

### --- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:
```
2199943210
3987894921
9856789892
8767896789
9899965678
```
Each number corresponds to the height of a particular location, where `9` is the highest and `0` is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a `1` and a `0`), one is in the third row (a `5`), and one is in the bottom row (also a `5`). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are `2`, `1`, `6`, and `6`. The sum of the risk levels of all low points in the heightmap is therefore `15`.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?


### --- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height `9` do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size `3`:
```
2199943210
3987894921
9856789892
8767896789
9899965678
```
The top-right basin, size `9`:
```
2199943210
3987894921
9856789892
8767896789
9899965678
```
The middle basin, size `14`:
```
2199943210
3987894921
9856789892
8767896789
9899965678
```
The bottom-right basin, size `9`:
```
2199943210
3987894921
9856789892
8767896789
9899965678
```
Find the three largest basins and multiply their sizes together. In the above example, this is `9 * 14 * 9 = 1134`.

What do you get if you multiply together the sizes of the three largest basins?
