# Approach
### Data format

I ended up writing this so that my actual data ends up being a `Grid` of the final output. So I take my input string
and loop over a 128 range to generate the 128x128 grid of `0`s and `1`s. I then take those values and construct a
`Grid` of them so that I can easily do neighbor checks.

### Part 1
> _Given your actual key string, how many squares are used?_

Originally I did this as a one-liner without using my `Grid` class and it ran really fast and gave the correct answer.
After reading part 2, though, I decided to have my `get_data` return a Grid, and so this one ended up being just a count
of how many nodes were `1` in my `Grid`. This was even more simplified by just adding up all the values in the `Grid`
since they were all either `1` or `0`...so the sum of `1`s will give me the number of used spaces.

### Part 2
> _How many regions are present given your key string?_

Once I had my grid initialized, this was pretty simple. All I do is loop over every node in the grid. When I get to a
`1` I do a basic BFS on the nodes from that one finding all neighboring values of `1` and then all their neighbor values
of `1` etc until I find all nodes in that group. I keep track of all nodes I have visited, which means all nodes that have
already been accounted for in a group, and just append each group I find to a list. Once I have gone through every node
in the grid, I end up having a list of groups...so just return the length of that list.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               2 |
| **Part Two** |              50 |
