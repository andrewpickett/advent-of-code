# Approach
### Data format

This one was fun to visualize. I probably didn't need to build the map exactly how the example outputs show, but it was
fun to actually build them that way.

Long story short, any time you start having branching and multiple paths that need traversed, you know you're going
to need to maintain a stack of branch positions.

I just iterate over each character in the regex and move my current position that direction. Whenever I see a `(` it means a
new branch possiblity, so I store the current position in a stack and continue processing. If I run into a `|` it means we're
done with that branch, so go back to the last position on the stack. Finally if I see a `)` it means pop the last position
off of the stack.

So that's how I get all of the positions of all of the rooms. I then actually build the map with walls and doors by
storing it into my Grid class -- which means I have to offset the values by the smallest negative number.

In the end, I just have a grid representation of the entire facility as well as my start point. Now I can do my grid
traversal algorithms.

### Part 1
> _What is the largest number of doors you would be required to pass through to reach a room?_

So it's stupidly slow, but I just go through every room and do an A* traversal back to the start node, storing the distance
in a map. Then I can just find the largest one in the map and done.

The problem is, I'm re-running the traversal for every room, even if it's been visited in previous runs, so it's really
really really inefficient (plus my algorithm probably isn't the fastest). So it takes an hour to run.

I will maybe go back and optimize it, but it worked and gave me the correct answer, so...yay me!!

### Part 2
> _How many rooms have a shortest path from your current location that pass through at least 1000 doors?_

Well...my algorithm works to find ALL distances...so just re-run it and count how many are above 1000. Unfortunately,
since my algorithm is dirt slow, this one also takes an hour to complete...

So in the end, I just ran part 1, outputting all of the distances, and then threw them all into excel to find how many
were >= 1000. But in theory the code checked in will also work, it'll just take forever.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |         3235645 |
| **Part Two** |         3235645 |
