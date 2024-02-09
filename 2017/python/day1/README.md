# Approach
### Data format

Read the input as a single string.

### Part 1
> _What is the solution to your captcha?_

Alright, well, just use a list comprehension to get the sum of all numbers where it matches the next one. To handle the
wrap around, I use a `mod` on the length of the input, so that when I check "current index + 1", it mods to 0, which
is the beginning of the list again.

### Part 2
> _What is the solution to your new captcha?_

Well, since I already am using `mod` to handle wrap around, I just change the offset to check from `1` to half the size
of the input. Make that one change and it just works.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
