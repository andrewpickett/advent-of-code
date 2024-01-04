# Approach
### Data format

I rewrote this to use my Grid/Point classes. This means I am able to just read the file directly into a data structure
that allows me to have a 2-d array of Points, which all are aware of their neighbor points. I then added this to a map
along with the number of steps I'm supposed to run (to allow for easier testing).

### Part 1
> _In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?_

I just read in the input into a new Grid and then use the helper methods in that to check and set neighbor values for each
step. At the end, just count the number of lights on in the grid.

### Part 2
> _In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?_

Pretty much no difference with this part, except I have a set of "broken lights" that I just don't include in my loop
of lights to check.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            1177 |
| **Part Two** |            1793 |
