# Approach
### Part 1
> _Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter??_

This puzzle initially looked like it was going to be a little tricky based on the input, but it ended up
being pretty simple. I decided to simply brute force this one first, because it would be pretty easy and
quick to do. However, this can all be done mathematically, so I'll probably go back and change it
later.

The biggest part to realize is that the repeating infinitely to the right of the map just means you need
to use modulus operator.

Read the lines in as an array of strings (which in python are just arrays of characters), and then
just check the value at each location along the line to see if it's a tree until you get below the bottom
of the map.

### Part 2
> _What do you get if you multiply together the number of trees encountered on each of the listed slopes??_

There was nothing "new" in this part of the puzzle. I just reused the same code as in part 1, but
for each of the slopes given and then multiplied together.

So, like I said, brute forced it, but nothing tricky here.

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 250  | 1  | <1  | 00:08:50  | 1943  |
| **Part Two**  | 1592662500  | 1  | 1  | 00:02:54  | 1287  |
