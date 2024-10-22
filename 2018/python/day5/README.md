# Approach
### Data format

Read the input as a string. Nothing else.

### Part 1
> _How many units remain after fully reacting the polymer you scanned?_

For every letter in the alphabet, just replace the combinations of lower+upper and upper+lower. Once it is found that
there were no substitutions, it means it can't be reduced anymore. So just do that and return the length of the
resulting string.


### Part 2
> _What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?_

Do the exact same thing as part one, but after removing each letter one at a time and then just keep track of the
smallest length.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             314 |
| **Part Two** |            7416 |
