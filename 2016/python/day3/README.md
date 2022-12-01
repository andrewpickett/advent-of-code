# Approach
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

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |    982 |        1 |               1 |                   N/A |  N/A |
| **Part Two** |   1826 |        1 |               1 |                   N/A |  N/A |


# Original puzzle
### --- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... `5 10 25`? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because `5 + 10` is not larger than `25`.

In your puzzle input, how many of the listed triangles are possible?

### --- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

```
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
```
