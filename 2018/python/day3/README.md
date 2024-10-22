# Approach
### Data format

Read each line into a list. While that's how the data is loaded, each part, it then gets parsed into the individual
pieces. I could probably do this in a much more elegant way, but this works for now.

### Part 1
> _How many square inches of fabric are within two or more claims?_

Just populate a 2d array with the claim numbers, and every time there's an overlap, set the value to `-1`. Then at the
end, just add the number of elements that have a `-1` value.

### Part 2
> _What is the ID of the only claim that doesn't overlap?_

Populate the 2d array just like before. Then just run through the input claims a second time and check if there are
any `-1` values in the range given. If there aren't, then return that claim number.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             226 |
| **Part Two** |             127 |
