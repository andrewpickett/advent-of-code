# Approach
### Data format

Alright, so read the data into a Grid. Then use a BFS to find the shortest distances between every number to basically
create a weighted graph. So the end result is a simple weighted graph connecting all nodes to each other with their
distances as the weight.

I represented this as a map of points that contains the point itself as well as a map of the distances from itself to every other point.
Something like this:
```
{
	0: {
		"p": Point(),
		"d": {
			0: 0,
			1: 2,
			2: 8,
			3: 10,
			4: 2
		}
	},
	1: {
		"p": Point(),
		"d": {
			0: 2,
			1: 0,
			2: 6,
			3: 8,
			4: 4
		}
	...
}
```

I used a simple BFS on my `Grid` class, since I already had one written. It could probably be much more optimized, but since
I only need to do this part once, it's fine.

### Part 1
> _Given your actual map, and starting from location 0, what is the fewest number of steps required to visit every non-0 number marked on the map at least once?_

Once I had the data into the data structure above, it is just a matter of getting all possible permutations of the paths that
are possible and summing up their distances. Find the one that has the least and that's the answer!

This really only worked because there were only 8 points in the path, which means there are only 7 points that can vary
as part of the path (since you always start at `0`). This means that there are only `7! = 5040` possible paths that can be taken.

### Part 2
> _What is the fewest number of steps required to start at 0, visit every non-0 number marked on the map at least once, and then return to 0?_

Well, all the hard work was already done by getting the distances between the points. There's nothing new in this part of the
problem except to add a return trip back home. So now my path both starts and ends with `0`. Run it and get the answer.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               9 |
| **Part Two** |               9 |
