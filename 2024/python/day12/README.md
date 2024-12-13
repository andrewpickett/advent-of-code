# Approach
### Data format

I decided to store the entire grid as a map (I'm really loving using maps now...so much faster!). The map is just `(y, x): value`.
This allows me to do very fast checks for if a point is in an existing region or not.

### Part 1
> _What is the total price of fencing all regions on your map?_

Ah, a good old flood-fill. This was one of the first algorithms I remember having to write for an AoC puzzle that after
I wrote it and solved the puzzle (back in 2019?), I found out it has an official name and is a well-known method...

Anyways, I just loop through every point on the grid (using the `keys` from the map) and do a flood-fill on it, checking
for all points connected to it with the same label. Once I have all of them in a given point's region, I remove those points
from my list of points that I need to visit.

When all is said and done, I end up with a list of `(label, set(points in region))` tuples. Now that I have that, the area
is just the length of that set in a region...and the perimeter is just the number of points in that region that has at least
one orthogonal neighbor NOT in the same region. Now just multiply area and perimeter and add up all the regions. Done.

I was pretty happy with how this one went.

### Part 2
> _What is the new total price of fencing all regions on your map?_

So the area is obviously still the same, but now we need to figure out how to count the number of sides. My first thought
(which I still think would work!) was to start at some point on the perimeter, find the wall and literally traverse the
perimeter. If you bump into a wall ahead of you, then turn, and keep following the wall and just count how many times
you have to turn to keep going -- basically following the "right hand rule" of traversing a maze.

I was spending way too much time trying to get the traversal to work correctly...but in the process of this, I realized
what I was doing in that process was actually counting the number of CORNERS in the region. I wrote a bunch of examples
down by hand and counted the number of sides and corners and verified that it was indeed true: the number of sides of
any region is equal to the number of corners...and I figured corners would be a lot easier to find.

So I started trying to get fancy with my use cases to count corners (again, I think I could figure it out!), but it was getting
late, and I was tired...so I instead decided to just explicitly write every use case I could think of. I came up with
8 distinct scenarios where a corner could be identified...so I just quickly did a bunch of if-statements for each use case.

And I let it fly...

To my complete shock, I got the answer right away...and I made it in the top 1000 again. So I'm pretty happy with how
it went.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             225 |
| **Part Two** |             479 |
