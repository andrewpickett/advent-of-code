# Approach
### Part 1
> _What is the distance of the shortest route?_

Alright, so creating the data structure is the important piece here, again. Since it's just a weighted graph, I created a
dictionary that has each city and their destinations like this:
```json
{
	city_a: {
		city_b: <distance>,
		city_c: <distance>,
		city_d: <distance>
	},
	city_b: {
		city_a: <distance>,
		city_d: <distance>
	}
}
```
While iterating over the input file, we add cities to the map and then add where they are connected to with their distance.
Whenever we add one one direction, we have to make sure to add it the other, so that way it becomes bi-directional.

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

# Original puzzle
### --- Day 9: All in a Single Night ---
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the **shortest distance** he can travel to achieve this?

For example, given the following distances:
```
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
```
The possible routes are therefore:
```
Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
```
The shortest of these is `London -> Dublin -> Belfast = 605`, and so the answer is 605 in this example.

What is the distance of the shortest route?

### --- Part Two ---
The next year, just to show off, Santa decides to take the route with the **longest distance** instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) `Dublin -> London -> Belfast`.

What is the distance of the longest route?
