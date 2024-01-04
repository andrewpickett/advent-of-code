# Approach
### Data format

I decided to just read the input as one giant string, since I'll just traverse over each character.

### Part 1
> _How many houses receive at least one present?_

This is really the first puzzle where we need to start "traversing" around a grid. So the first thing I wanted to figure
out was how to represent the position and how to easily represent directional navigation.

The grid was easy enough for this puzzle, since we don't need to worry about any neighbors or anything like that, we can
just keep track of our current position using a tuple of `(x, y)` coordinates.

For the directional navigation, I decided to just create a map of movements. Each character maps to a change in position
after being applied. So for example, `v` means "go down" so the _movement_ is a change of `-1` in the y direction and `0`
in the x direction. This means it can be represented with a change tuple of `(0, -1)`.

Once those were in place, it was just a matter of iterate over all characters in the input and apply their movements to them,
keeping track of the current position. Whenever you move, add that new position to a `set()`, and in the end, you have
the total number of positions visited.

### Part 2
> _This year, how many houses receive at least one present?_

Part two actually isn't much different than part 1. The only difference is that we have to keep track of 2 different "current
positions" and alternate the movements between the two. So really, just make it in array of position tuples and a tracker for
which mover is being used is all that's needed to make this one work.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               5 |
| **Part Two** |               7 |
