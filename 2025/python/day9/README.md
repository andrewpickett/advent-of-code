# Approach
### Data format

I created a few utility classes for collision detection. Some of these are similar to my `Grid` classes (e.g. `Point`),
but I felt they would have specialized usage and hopefully I'll be able to use them in other puzzles by expanding
them to different dimensions, etc.

But I pretty much just read the input file in as a list of `Point2d` objects...which just hold `x` and `y` coordinates.

### Part 1
> _what is the largest area of any rectangle you can make?_

This one is pretty simple: just calculate the area of the rectangle created by any given two points and return the
maximum. I just loop over every single combination of points and calculate and return. Runs fast enough for me.

### Part 2
> _what is the largest area of any rectangle you can make using only red and green tiles?_

So, for this part, I pretty much just loop over every combination of points and create a `BoundingBox` for each pair.
This helper class just takes two points, figures out the orientation of them by finding all 4 corners, determining
all 4 edges, and allows calculating the area.

To do this, I also created a `Line2d` class. So I then have a `Point2d`, `Line2d`, and `BoundingBox` classes.

Now, for each `BoundingBox` defined by any two points, I check if the entire box exists INSIDE of the polygon defined
by the input points. If it is, then I check for the largest area and return it.

Ok, so a few things we need to be able to check:
1) A given point is on a given line segment. We can do this by checking collinearity and boundedness.
2) A given point is inside any given polygon. For this, I use a simple ray casting algorithm to determine the number of times a ray passes through the edges of the polygon (if odd, then it's inside; if even, it's outside).
3) If two given line segments intersect anywhere. For this, I use an orientation function to help determine if any points lie on opposite sides of a segment, and therefore if they intersect.

So now, given those 3 capabilities, checking if a `BoundingBox` is completely inside of a polygon, we can simply do the
following:
1) Check each corner of the box to see if the points are in the polygon (points 1 and 2 above)
2) The box's edges intersect with the polygon's edges at any given point (point 3 above)

If #1 is true and #2 is false, then we know the box has to be completely in the polygon. And I do them in that order, because
#1 will eliminate a lot of boxes very quickly, while #2 above takes a bit more work to determine.

It still doesn't run super fast (especially with CPython!), but for now I'll take it!

# Results

|              |          Exec. Time (ms) - Python 3.13 |       Exec. Time (ms) - PyPy 3.11 |
|--------------|---------------------------------------:|----------------------------------:|
| **Get Data** |                                  0.724 |                             1.596 |
| **Part One** |                                133.743 |                            10.470 |
| **Part Two** |                             138261.488 |                          3903.754 |
| **TOTAL**    |                           *138395.955* |                         *3915.82* |
