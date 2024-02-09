# Approach
### Data format

Just read the input as a single int.

### Part 1
> _How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?_

Good ol' maths...

I start by figuring out which "ring" my number would be in. Each ring's highest value is simply powers of odd numbers:
`1, 9, 25, 49, ...`. So I find which ring has a value higher than my number and so then I know my upper and lower bound.

Next I create a list of all of the distances for each point in that ring to the center. It starts at `2*x` where `x` is the
ring number because the corner would be `x` units down and `x` units across from the center at that point. It then decrements
until it's directly under the center which is `x` units away. Then increments back up to `2*x`. This continues for each of the
for sides of the ring.

Now, I just start walking backwards from the last value until I am at my input value and then look up the distance in my
distance array! Done!

### Part 2
> _What is the first value written that is larger than your puzzle input?_

For this part, I actually just start building out the points starting from the middle. I keep a dictionary of points so that
I know which ones have already been initialized and as I go around I just get all of the possible neighbors for the next point,
see if it's been defined yet, and if so, add it up to get the new value of the current node. Keep doing that until I have
a value higher than my input.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
