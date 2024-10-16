# Approach
### Data format

I really just needed to keep a list of infected points. I don't need to know any points that aren't infected, so just
iterate over the input data and add points to a list that are infected. Now, I decided to make the origin the very
center of the input and "up" and "left" are -1 on the y and x axis respectively. Now the other odd thing is my coordinates
are backwards in that they read (y, x) position -- so sue me.

After getting to part 2, I realized I would also need maintain a state. So I updated the list to be a dictionary.
I still don't keep values for "clean" nodes, and just initialize all infected with a state of "INFECTED". So now I
can maintain the state of any given nodes and just remove them when they are cleaned.

### Part 1
> _Given your actual map, after 10000 bursts of activity, how many bursts cause a node to become infected?_

Literally just write what the steps are. I had a helper utility for changing directions, so I decided to use that...
but other than that, I just start at (0, 0) facing "up" and iterate over the number of bursts specified.
When I infect a node, keep a counter and return that. Pretty simple!

### Part 2
> _Given your actual map, after 10000000 bursts of activity, how many bursts cause a node to become infected?_

Ok, 10 million is a lot of iterations...but I figured it might not be TOO many. I updated my map and movements to
include the new rules and decided to just let it fly!

After only 16 seconds it completed and everything worked just fine. I could try to improve it, but I'm fine with it
for now.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              12 |
| **Part Two** |           16432 |
