# Approach
### Data format

My first pass at this one had me using my `Grid` class. It seemed like a natural choice, based on the type of input data.
It actually worked just fine...I read it in, found the start point, and used the `Grid` methods to get and set values
and move the beams through the grid.

After finishing the puzzle, I realized it was WAY overhead, since I only ever needed to get the values to the right
and left of the splitters...so I can just use a basic 2D array, which is going to be MUCH faster.

### Part 1
> _How many times will the beam be split?_

At first, I actually fired a beam from the start, kept a `set` of all of the active beams, and I would just keep popping
them off of the `set` until there were none left. Every time I hit a splitter, I added 2 new beams to the set.

This worked pretty well, especially with my `Grid`, since points wouldn't be duplicated. Again, though, once I realized
how much overkill my original approach was, I rewrote it completely.

Basically, I just take it line by line (since once the beams leave a given line, they don't ever have to go back up for
any reason). Whenever I run into a `^`, just add to the number of splits. Then move to the next line and process it...
nothing else to it really.

### Part 2
> _In total, how many different timelines would a single tachyon particle end up on?_

Again, I originally had it working with my `Grid`, and swapped out the `set` for a `dict`, but during my rewrite, I realized
it's pretty much the same thing as part 1, but just keep a dictionary of the number of times any given point is hit by a
split. So, since I'm just keeping track of counts in a `dict`, it runs extremely fast!

# Results

|              |     Exec. Time (ms) - Python 3.13 |     Exec. Time (ms) - PyPy 3.11 |
|--------------|----------------------------------:|--------------------------------:|
| **Get Data** |                             0.366 |                           0.431 |
| **Part One** |                             2.988 |                           0.684 |
| **Part Two** |                             2.940 |                           0.723 |
| **TOTAL**    |                           *6.294* |                         *1.838* |
