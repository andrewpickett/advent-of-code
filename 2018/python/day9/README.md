# Approach
### Data format

Just read the first and second to last parts of the input as integers and store them for use.

### Part 1
> _What is the winning Elf's score?_

First I tried just using an array and doing the moving of the pointer manually over and over. It worked...and this part
ended up running in under 0.5 seconds, so I thought it was pretty good. Once part 2 came into play, it just kept running
forever, so I decided I needed a faster/better way.

I always forget about the `deque` in python. But once I remembered it, and that it has a `rotate()` function, which does
EXACTLY what this puzzle needs, I tried implementing with it. It made the code a whole lot simpler, and better yet,
part 1 ran in a few milliseconds. So I knew part 2 would actually work now...

### Part 2
> _What would the new winning Elf's score be if the number of the last marble were 100 times larger?_

Exactly the same, just multiply the number of marbles by 100 before running.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              14 |
| **Part Two** |            1625 |
