# Approach
### Data format

Just read the input as a string.

### Part 1
> _Using the initial state in your puzzle input, what is the correct checksum?_

Just did everything the instructions said. I didn't do anything fancy here. It solved immediately, so I went with it.

The only "fun" part of it was how to switch the bits from 0s to 1s and vice versa. I decided to use an XOR command, which
I thought was pretty slick and it worked quite well.

### Part 2
> _ Again using the initial state in your puzzle input, what is the correct checksum for this disk?_

Didn't change a thing -- it took longer to finish, but still a reasonable amount of time, I guess. I'm SURE there are
optimizations and mathematical ways to improve it, but I'm fine with this for now.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |           25805 |
