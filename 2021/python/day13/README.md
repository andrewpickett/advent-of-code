# Approach
### Part 1
> _How many dots are visible after completing just the first fold instruction on your transparent paper?_

My ranking on this one wasn't great, because I didn't start it until the next morning...I wish I would have stayed up
for it, though because I solved both parts REALLY fast...

There actually wasn't very much to think about with this puzzle. I already wrote my Grid and Point classes, so I figured
I would just use those (mainly because my Point class already had ways to update coordinates as well as comparison methods,
which I knew I would need).

But the idea was that when you do a horizontal fold, you just need to find all of the points "below" the line you're
folding on. Then take the vertical distance between the point and the line and subtract it from the line. That new
vertical position is where your point ends up. So just do that for all of them, keep them in a set (so that if you
land on top of another point, it just doesn't count) and you're done with a "fold".

For this part, they just asked for a count of the dots, which ends up being the size of the resulting set. Simple

### Part 2
> _What code do you use to activate the infrared thermal imaging camera system?_

Everything is already done to handle all of the folds. So I just ran the same code but for all of the folds in the
instructions. Once that was done, I needed to SEE the resulting matrix...so I used my Grid class to add all of the points
and use the `__str__` method I already wrote to output it. Nothing difficult.

# Results

|              |   Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) |  Rank |
|--------------|---------:|---------:|----------------:|----------------------:|------:|
| **Part One** |      737 |        1 |               3 |             ~00:07:00 | 23175 |
| **Part Two** | ZUJUAFHP |        1 |               5 |             ~00:04:00 | 22024 |

# Original puzzle

### --- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:
```
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
```
The first section is a list of dots on the transparent paper. `0,0` represents the top-left coordinate. The first value, `x`, increases to the right. The second value, `y`, increases downward. So, the coordinate `3,0` is to the right of `0,0`, and the coordinate `0,7` is below `0,0`. The coordinates in this example form the following pattern, where `#` is a dot on the paper and `.` is an empty, unmarked position:
```
...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
```
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal `y=...` lines) or left (for vertical `x=...` lines). In this example, the first fold instruction is fold along `y=7`, which designates the line formed by all of the positions where `y` is `7` (marked here with `-`):
```
...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
```
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:
```
#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
```
Now, only `17` dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at `0,0` and `0,1`). Because the paper is transparent, the dot just below them in the result (at `0,3`) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along `x=5`, which indicates this line:
```
#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
```
Because this is a vertical line, fold left:
```
#####
#...#
#...#
#...#
#####
.....
.....
```
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?

### --- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?
