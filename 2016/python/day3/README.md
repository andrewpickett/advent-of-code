# Approach
### Data format

Read each line of input as a tuple of side lengths into an array. Something like:
```
[
	(3, 4, 5),
	(5, 12, 13),
	...
]
```

### Part 1
> _In your puzzle input, how many of the listed triangles are possible?_

I went with a basic approach: read a line of data, sort them, add the two smallest numbers. If the sum is less than the largest,
then that row is not a triangle.

I then went back and just cleaned it up and made it more concise. I used some basic algebra to reduce the equation for comparison
to just use the `sum` and `max` of the lines (if the total sum of sides is less than or equal to 2 * the max side length, it's not a possible triangle).

This allowed me to do everything in a nice little list comprehension.

### Part 2
> _In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?_

Just read in 3 rows of data at a time and for each of those 3 rows, read all three columns. Do the same calculation as
in part one.

Really no additional "trickery" here.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               1 |
| **Part Two** |               1 |
