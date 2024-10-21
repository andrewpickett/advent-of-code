# Approach
### Data format

Alright, the basic idea for the way to think through this problem is as a graph (more explanation as to why in the Part 1
section below). But, since we don't actually need the connections, I decided to just keep a list of all of the points
as well as a list of all of the possible starting points (those that have a `0` in them).

### Part 1
> _What is the strength of the strongest bridge you can make with the components you have available?_

First step is that we need to run some algorithm from each and every starting node (nodes that have `0` in them).
As such, we know we're going to loop over those possible starts. I then decided to simply do a depth-first traversal
of the "graph" created by conceptually linking the nodes together without any repeats. Whenever we get to a point
where there are no possible remaining nodes "connected", we simply add that path to the list of possible paths.

In the end, we will end up with a list of all possible paths. We don't care about fragments of a path, since we are only
looking for the "longest" (e.g. `0/1` doesn't matter once we have `0/1 --> 10/1`...because there's no way `0/1` could
ever be longer by itself). So, we only need to store fully developed paths.

Once the list of all possible paths is complete, just find the one that has the highest weight. Done. It takes a little
while to run, but it's not too horrible.

### Part 2
> _What is the strength of the longest bridge you can make?_

Well, since I have all of the paths, just loop over them saving the longest ones. Then at the end just get the weights
of these longest ones. Done and done.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            4088 |
| **Part Two** |            3076 |
