# Approach
### Data format

I split the input on `, ` so that it gives me a list of instructions. I then broke those up into tuples of the direction
and the integer amount. That way I can just easily use those values while traversing.

### Part 1
> _How many blocks away is Easter Bunny HQ?_

This was a surprisingly tricky first day puzzle! Conceptually, it was
pretty easy, just keep track of your x-y coordinate as you traverse through each data point...but to do that, you need
to keep track of your orientation and then move.

This first part wasn't hard, but definitely took a little care when writing it up.

### Part 2
> _How many blocks away is the first location you visit twice?_

So it seemed just as simple as the first part, and so I wrote it up where I just kept track of all the points I visited
and if I see the same point, return it. Done.

Wrong answer.

I didn't pay close enough attention to their specific example, which showed that it wasn't just the END points that mattered
for visiting, but any points you cross while travelling between two places! So, instead of keeping track of just the end
points in a list, as it moves from one point to the next, you need to keep track of every point you cross along the way.
At this point, once you see the same point in the list, you can just return that one.

Again, for a first day puzzle, this one was much trickier than any others I've done.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
