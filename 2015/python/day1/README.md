# Approach
### Data format

I decided to just read the input as one giant string, since I'll just traverse over each character and use the `.count()`
function

### Part 1
> _To what floor do the instructions take Santa?_

Since `(` is `+1` floor and `)` is `-1` floor, just subtract the number of `)` from the number of `(` in the input
and it will give you the resulting floor.

### Part 2
> _What is the position of the character that causes Santa to first enter the basement?_

Just iterate through the input and add/subtract based on each character. Once you have a value of `-1`, return the
index you're on plus one (because of 0-based indexing).

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
