# Approach
### Data format

Just read the input as a number.

### Part 1
> _What is the value after 2017 in your completed circular buffer?_

I actually keep an array with the values that get inserted as well as my current position in the array. Build the array
exactly how they describe it in the instructions. It was very fast, so it works quite well.

### Part 2
> _What is the value after 0 the moment 50000000 is inserted?_

Obviously I can't build a 50 million element array and expect it to ever finish. Luckily with this part of the puzzle,
you just need to know what's in the array at index `1` -- because once `0` is inserted at the `0` index, it CAN NEVER MOVE.
So to know what's next to zero is just always the `1` index. This means I just need to track when my current position
is `1` and keep track of what value would be going there. Do that through all 50 million iterations and just return the last
value that would have been inserted.

I may be able to optimize it more/better, but 10 seconds isn't bad.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |            9546 |
