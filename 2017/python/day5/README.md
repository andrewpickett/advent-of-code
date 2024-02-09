# Approach
### Data format

Read the input as an array of integers.

### Part 1
> _How many steps does it take to reach the exit?_

Just keep a pointer to the current instruction you're on. Increment the current value by `1` in the array and then increment
your pointer by the original value in that position. If ever you're less than 0 or more than the size of the array, then quit
and return the number of steps.

### Part 2
> _How many steps does it now take to reach the exit?_

Do the exact same thing, but instead of just incrementing by 1 every time, do a quick check to see how much to increment by.
I used a lambda function as a parameter to my code so that I can reuse parts 1 and 2.

I needed to make sure to pass COPIES of the original data to the code, as by nature these algorithms change the values in the
original integer array.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             147 |
| **Part Two** |           10704 |
