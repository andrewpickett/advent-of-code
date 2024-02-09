# Approach
### Data format

Read the input as an array of integers.

### Part 1
> _Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a configuration is produced that has been seen before?_

Nothing fancy here...just look at the numbers, find the highest value and its index in the array. Then set that value to 0 to
"empty" it. Now, take that highest value and divide by the size of the array and add that whole amount to every single block.

That leaves us with SOME amount left over. Just incrementally add 1 to each of the following banks.

Do this over and over until an existing combination has been seen (being kept track in an array).

### Part 2
> _How many cycles are in the infinite loop that arises from the configuration in your puzzle input?_

Do the exact same thing, but actually return the array of all the combinations. Then look for the index of the first
occurrence of the combination and subtract it from the length of the array. Done.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             302 |
| **Part Two** |             295 |
