# Approach
### Data format

I read the data in as a 2d array of integers. Read each line and split it by spaces and then cast each value to an int.

### Part 1
> _What is the checksum for the spreadsheet in your puzzle input?_

Just sum up each of the `max() - min()` for each row in my 2d array. Super simple.

### Part 2
> _What is the sum of each row's result in your puzzle input?_

Slightly more complicated, but still just a sum of the `max() / min()` for any that cause `max() % min() == 0`. So it's
basically looping over every value with every other value and when I get to any that are evenly divisible, just add
it to the sum -- exactly as described in the problem.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
