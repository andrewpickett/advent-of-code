# Approach
### Data format

Alright, so creating the data structure is the important piece here, again. Since it's just a weighted graph, I created a
dictionary that has each city and their destinations like this:
```json
{
	"city_a": {
		"city_b": 1234,
		"city_c": 4321,
		"city_d": 111
	},
	"city_b": {
		"city_a": 1234,
		"city_d": 88
	}
}
```
While iterating over the input file, we add cities to the map and then add where they are connected to with their distance.
Whenever we add one one direction, we have to make sure to add it the other, so that way it becomes bi-directional.

### Part 1
> _What is the distance of the shortest route?_

Ok, so now that we have our graph as a map object, we can begin the algorithm to find the answer...and graph traversals are
typically recursive. So that's what I did. Basically I did a depth first search starting from each node and "ending" when all nodes are
in my "visited" list.

I then picked the lowest total value. Since I didn't need to keep track of the actual path traversed, and only the weight,
it was pretty simple to track.

### Part 2
> _What is the distance of the longest route?_

...Well, it's exactly the same, but instead of finding minimum value, just find the maximum. Same algorithm, though.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             197 |
| **Part Two** |             188 |
