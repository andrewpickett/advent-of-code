# Approach
### Data format

Just read the input as a string.

### Part 1
> _Given your vault's passcode, what is the shortest path (the actual path, not just the length) to reach the vault?_

This certainly screams BFS, doesn't it?

Well, that's exactly what it turns out it is. The main difference here is that instead of disallowing visiting the same
nodes twice, we allow it (since the open doors could change based on the hash). This means we just need to run through
EVERY possible path and then once we've done that, we can just find the one that's the shortest length.

Because of the fact that we don't revisit nodes, I had to rewrite a custom BFS instead of using the one I created
in my utils...but it wasn't bad.

### Part 2
> _What is the length of the longest path that reaches the vault?_

Didn't change anything. I already had every single path through the rooms, so instead of finding the shortest,
I find the lengths and return the maximum. Nice and easy.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             149 |
| **Part Two** |             158 |
