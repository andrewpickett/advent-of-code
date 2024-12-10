# Approach
### Data format

Well, once again, I was really excited to use my `Grid` class...it made reading in the data very simple...and I was able
to do a BFS right away for part 1. It worked great...but then I realized modifying my BFS to work for part 2 on my `Grid`
was going to be more work than just writing a new BFS using native arrays.

So, because this keeps happening to me, I decided to write a new utility method to read in the input into just a 2d array.
I wrote one that handles strings, and one that handles ints. As part of this utility, I added the ability to pad the array
so that I don't have to worry about edge cases as much.

When all is said and done, I end up with just the input as a 2d array of ints padded with -1 values around the edges.

### Part 1
> _What is the sum of the scores of all trailheads on your topographic map?_

Hello BFS, it's nice to see you! This is actually a VERY simple implementation of a BFS, in that we just continue
to add neighbors of nodes to a queue when they are EXACTLY 1 higher than the current. We start with all of the nodes that
are `0`s. From there, we just pop off the items
of the queue and keep adding their neighbors. We're done when the queue is empty, and we keep a counter of how many times we see a `9`.

We need to make sure to keep track of any that we've already seen before, in the case where two of the start nodes end
at the same end node. We don't want to double count them afterall...


### Part 2
> _What is the sum of the ratings of all trailheads?_

Alright, I lied -- now we DO want to double count them. We want to count each and every path from `0` to `9`, regardless
of if it's been traversed by another trailhead. Just add an `if` condition to ignore the visited set and part 2 is solved.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              26 |
| **Part Two** |              24 |
