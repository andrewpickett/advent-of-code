# Approach
### Data format

Just read the input as a string and store it in a map so that I can change the row count for testing.

### Part 1
> _Starting with the map in your puzzle input, in a total of 40 rows (including the starting row), how many safe tiles are there?_

Just do exactly as the instructions say: while building the next row, use their logic to determine which spaces are safe
and which are traps. Now, since we don't actually need to keep track of the entire room, just the previous row, we
just need to remember that one and since it's just asking for a count of safe tiles, we can just count as we go.

It's fast for this part of the puzzle, but I'm sure part 2 will bite me.


### Part 2
> _How many safe tiles are there in a total of 400000 rows?_

Actually, no difference here. It's not fast, but it works just fine and doesn't take up a bunch of CPU or memory.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |           25123 |
