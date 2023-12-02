# Approach
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

# Original puzzle
### --- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (`^`), south (`v`), east (`>`), or west (`<`). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive **at least one present**?

For example:
* `>` delivers presents to `2` houses: one at the starting location, and one to the east.
* `^>v<` delivers presents to `4` houses in a square, including twice to the house at his starting/ending location.
* `^v^v^v^v^v` delivers a bunch of presents to some very lucky children at only `2` houses.

### --- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, **Robo-Santa**, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive **at least one present**?

For example:
* `^v` delivers presents to `3` houses, because Santa goes north, and then Robo-Santa goes south.
* `^>v<` now delivers presents to `3` houses, and Santa and Robo-Santa end up back where they started.
* `^v^v^v^v^v` now delivers presents to `11` houses, with Santa going one direction and Robo-Santa going the other.
