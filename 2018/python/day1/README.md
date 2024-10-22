# Approach
### Data format

Store each number from each line in the input as a list

### Part 1
> _Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?_

Just have to add up all the numbers in our list. That's it.

### Part 2
> _What is the first frequency your device reaches twice?_

Not much more to it, except we just need to keep running through the list over and over and over keeping track of all
of the total frequencies we've ever seen. Once we run across one that we've seen before, just return that value.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              94 |
