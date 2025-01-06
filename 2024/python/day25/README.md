# Approach
### Data format

Read each pattern into a 2d array. I then rotate each of them 90 degrees so that its easier to analyze later. I then
divide them into two different groups: keys and locks.

### Part 1
> _How many unique lock/key pairs fit together without overlapping in any column?_

Really, all we need to do for this one is to loop over each lock and key and check each row within them to make sure they
the total number of `#` matches the length of the row (meaning the key exactly fits in the lock). Do that for every
single lock/key combination and keep track of the total.

### Part 2
> __

Push the button, and it is done! Another successful year!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             149 |
| **Part Two** |             N/A |
