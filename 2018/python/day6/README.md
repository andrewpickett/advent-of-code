# Approach
### Data format

There's a decent amount of information we need: the total distance maximum for part 2, the list of all points from the
input, and the range of points that we actually care about. So I read in the points, then calculate the ranges for them
and store it all in a dictionary that can be passed around. It looks something like this:

```
{
	"d": 10000,
	"a": [(x1, y1), (x2, y2), (x3, y3), ..., (xn, yn)],
	"r": {
		"x": (minx, maxx),
		"y": (miny, maxy)
	}
}
```

### Part 1
> _What is the size of the largest area that isn't infinite?_

Ok, well, the two parts we need to start this are the fact that we know we don't have to check outside of the range
of points for locations -- since any locations outside of the range of points would always be infinite. The other part
is that we need to identify OTHER regions that are infinite, and we can find that by just getting any regions that exist
on the boundary. If a region exists on the boundary, then it will always keep going further out...meaning it's infinite
and can be removed from the list of points we care about.

So...now that we know that, it's just a matter of iterating over every single point in our bounded range and calculating
the distance to each point. If there is just a single point for a given location AND it's not on the boundary, we can
say that point needs to be included. Once we've done that, we can just count the number of times each point is referenced
and then pick the highest one...

It's a bit complicated to describe, but that's pretty much it.

### Part 2
> _What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?_

This one was much easier. This one is just iterating over each point again within the region and calculate the sum of
the distances to each point. Then just count how many of them are under our threshold. Pretty simple.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            1707 |
| **Part Two** |            1178 |
