# Approach
### Data format

Read the input as a list of directions (split input on `,`).

### Part 1
> _you need to determine the fewest number of steps required to reach him._

For this part, I just looked at the results of combining 2 different "steps" and what that ends up meaning. The below were
the mappings for two moves mapping to another:
* `n` + `sw` == `nw`
* `n` + `se` == `ne`
* `s` + `ne` == `se`
* `s` + `nw` == `sw`
* `se` + `sw` == `s`
* `ne` + `nw` == `n`
* `n` + `s` == `ne` + `sw` == `nw` + `se` == NO MOVEMENT

So, I basically just get counts of each of the movements, replace them as needed and cancel out ones that do that.

In the end, I have the "remaining" moves that just take you further away...so just add them all up and you have the
distance away.

### Part 2
> _How many steps away is the furthest he ever got from his starting position?_

Bummer. I was hoping my slick solution above would have simply led me to be able to answer part 2 right away.

Oh well...

Because I would need to keep track of the distance for EVERY stop along the path, I realized I would need to figure out
how to represent distance on a hexagonal plane. So I started writing down a coordinate system for each movement, and I got
something like the below:
```
(-2, 6)         (0, 6)        (2, 6)
        (-1, 5)        (1, 5)
(-2, 4)         (0, 4)        (2, 4)
        (-1, 3)        (1, 3)
(-2, 2)         (0, 2)        (2, 2)
        (-1, 1)        (1, 1)
(-2, 0)         (0, 0)        (2, 0)
        (-1,-1)        (1,-1)
(-2,-2)         (0,-2)        (2,-2)
        (-1,-3)        (1,-3)
```
Basically, any east/west adds/subtracts 1 to the x coordinate, any north/south adds/subtracts 1 to the y coordinate unless it is
by itself (e.g. `n` or `s`), in which case it adds/subtracts 2 to the y coordinate.

So that makes it easy to traverse and get a "coordinate" for any given position after movements. The next step is to figure out
how to determine distance in this new plane.

There are really 2 scenarios and it has to do with how vertical and diagonal movement work. If we don't have to move vertically
more than horizontally, then we can get to the node by just doing diagonal movements in that direction. In otherwords:
if the y coordinate is less than the x coordinate, then the distance is just going to be the x coordinate (absolute value in all cases).
Otherwise, we travel diagonally as far as we can towards the point and then directly up/down the remaining amount.

That's really it. Do that calculation for every step along the way and return the maximum.

Once I rewrote with this approach, I went back and changed part 1 to just return the last element in the distance list...
for consistency.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               6 |
| **Part Two** |               6 |
