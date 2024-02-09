# Approach
### Data format

Read each line as an array of strings, split by spaces.

### Part 1
> _How many passphrases are valid?_

Fairly straightforward of just check if the array of words equals the set of the same words. Any duplicates will drop out
of the set, and they won't be equal. Only if they are all unique would they be equal. Count all of those up.

### Part 2
> _Under this new system policy, how many passphrases are valid?_

For this part, I take each word on each line and sort the letters alphabetically. Once I have all of the strings re-arranged
alphabetically this way, I do the same logic I did in the first step and check if the set matches the original list.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |               2 |
