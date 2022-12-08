# Approach
### Part 1
> _Consider your map; how many trees are visible from outside the grid?_

So there were a few ways to approach this puzzle. I started by thinking I would check from the "outside" of the array
looking in to see how far I could see at each square. Basically, I was going to create a new array of the same size that will
track if each tree is visible or not. So I would iterate over each row and check "from the left". If I could see a tree, I would
increment a counter in the new array and keep going until I could not see a tree. At which point I would stop looking on that
row and move down. So for the example input we were given, I would end up with something like this:

_**Looking from the left**_
```
--> 30373					10010
--> 25512					11000
--> 65332		gives		10000
--> 33549					10101
--> 35390					11010
```

I was then going to look from the top, and I only care about entries that are 0, because if there are any that are already 1,
they are already visible...So the next iteration would look like this:

_**Looking from the top**_
```
|||||
vvvvv
30373					11111
25512					11100
65332		gives		10000
33549					10101
35390					11010
```

So do that approach on all 4 sides, then you can just count the number of 1s in your resulting array.

Now, like I said, I WAS going to do it that way, but I decided to go from the "inside" and work my way out instead.
The difference here is I just iterate over every entry in the array and then check all 4 directions, starting left and moving
clockwise, to see if any given square is visible. This more closely matches how the original problem was written, but I was afraid
performance was going to be a problem in part 2.

Now, I did do some optimization by not checking all 4 directions and stopping after any of them are visible. Once I decided
on this approach, and I fixed a couple of bugs with my indexing, the resulting code was pretty quick and seemed to work well.

Boy was I glad I went with this approach, because it made part 2 a lot easier!

### Part 2
> _Consider each tree on your map. What is the highest scenic score possible for any tree?_

Pretty much the exact same code as part 1. The key here is that we're not counting visible trees, but how far we can see. The same approach applied
as in part 1 (working from the inside outward), but this time I had to actually do all 4 directions and return a number instead
of a boolean. I initially copied the methods I had and change the return values from a simple
`True`/`False` to return an integer value that was the number of trees less than the current square. Once I again fixed a couple
little bugs, I got the correct answer. I then realized my methods were pretty much identical, so I rewrote them to reduce the code
and simply pass a flag on which return type I wanted to give.

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |   1662 |        3 |              24 |              00:31:22 | 5826 |
| **Part Two** | 537600 |        3 |              29 |              00:08:36 | 3623 |


# Original puzzle
### --- Day 8: Treetop Tree House ---
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these
trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number
of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

```
30373
25512
65332
33549
35390
```

Each tree is represented as a single digit whose value is its height, where `0` is the shortest and `9` is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees
in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view.
In this example, that only leaves the interior nine trees to consider:

* The top-left `5` is visible from the left and top. (It isn't visible from the right or bottom since other trees of height `5` are in the way.)
* The top-middle `5` is visible from the top and right.
* The top-right `1` is not visible from any direction; for it to be visible, there would need to only be trees of height `0` between it and an edge.
* The left-middle `5` is visible, but only from the right.
* The center `3` is not visible from any direction; for it to be visible, there would need to be only trees of at most height `2` between it and an edge.
* The right-middle `3` is visible from the right.
* In the bottom row, the middle `5` is visible, but the `3` and `4` are not.

With `16` trees visible on the edge and another `5` visible in the interior, a total of `21` trees are visible in this arrangement.

### --- Part Two ---
Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same
height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle `5` in the second row:

```
30373
25512
65332
33549
35390
```

* Looking up, its view is not blocked; it can see 1 tree (of height 3).
* Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
* Looking right, its view is not blocked; it can see 2 trees.
* Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is `4` (found by multiplying `1 * 1 * 2 * 2`).

However, you can do even better: consider the tree of height `5` in the middle of the fourth row:

```
30373
25512
65332
33549
35390
```

* Looking up, its view is blocked at `2` trees (by another tree with a height of `5`).
* Looking left, its view is not blocked; it can see `2` trees.
* Looking down, its view is also not blocked; it can see `1` tree.
* Looking right, its view is blocked at `2` trees (by a massive tree of height `9`).

This tree's scenic score is `8` (`2 * 2 * 1 * 2`); this is the ideal spot for the tree house.
