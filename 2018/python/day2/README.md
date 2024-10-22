# Approach
### Data format

Read each line in the file to a list. Nothing fancy here.

### Part 1
> _What is the checksum for your list of box IDs?_

Iterate over every line and for each word, get the count of every character in that string. Specifically, just keep
track of the characters whose count is 2 or 3. Then at the end of each word, calculate the checksum and add it all up.

### Part 2
> _What letters are common between the two correct box IDs?_

For this one, I do a bubble-sort type comparison over all of the items (i.e. comparing each one to every other). If at any
point I see more than one difference, I can just skip to the next. Once I find two words that are exactly one character
different, just remove that character and return it.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               9 |
| **Part Two** |              89 |
