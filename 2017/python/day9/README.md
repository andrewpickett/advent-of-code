# Approach
### Data format

Just read in the string.

### Part 1
> _What is the total score for all groups in your input?_

I really just read through the string, one character at a time. As I go, I keep track of the depth of the group I'm in.
If I run into an `!` I just increment the pointer an additional step (skipping the next character). I also keep track of
if I'm in garbage or not. As I go, I keep adding the depth of my group to a list so that I can just add them all up at the end.

So in the end, I have a count of garbage characters and a list of the group scores. So for this part, just return the sum
of the group scores.

### Part 2
> _How many non-canceled characters are within the garbage in your puzzle input?_

My garbage. Already have it...just return it.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               4 |
| **Part Two** |               7 |
