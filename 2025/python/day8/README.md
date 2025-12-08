# Approach
### Data format

Well, the current state of the code is very different than what I had originally. It turns out, though, that in the current
iteration of the code, the data format is the most time-intensive portion of the code. I knew I was going to need to
at least store the number of links to make, the list of coordinates from the input file, and the calculated
distances for every point to every other.

Getting the distances was going to be `O(n^2)` time...which isn't great, but since we only have 1000 entries in the input,
I figured it should be fine.

I then decided to just sort the distances in this section, since I knew I would need it for both parts.

So in the end, my data looks like this:

```json
{
	"coords": [(x1, y1, z1), (x2, y2, z2), ...],
	"distances": [(dist1, coord1, coord2), (dist2, coord3, coord4), ...],
	"links": 1000
}
```

### Part 1
> _what do you get if you multiply together the sizes of the three largest circuits?_

I decided to implement a fairly basic `merge-find set`, which just works with non-overlapping sets and has the ability to
find a set for a given item, merge sets, etc.

Using this, I just run merges on the data, keeping track of the number of connections made, for as many steps as needed.
As connections are made, keep track of the size of their circuit. Once we hit the number of connections needed, just
sort the data and return the product asked.

### Part 2
> _What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?_

Honestly, just run the same code without an end step. Once we reach the end of the coordinates (all of the data), we can just
return the product asked. It was the same code as part one, except at this point I had to put part one's limit check in
a conditional statement so that I could re-use the same code for both parts. Really not hard. Part 1 and the data were
definitely the harder parts of this puzzle...

# Results

|              |        Exec. Time (ms) - Python 3.13 |        Exec. Time (ms) - PyPy 3.11 |
|--------------|-------------------------------------:|-----------------------------------:|
| **Get Data** |                             1691.643 |                           2585.204 |
| **Part One** |                                4.777 |                             39.542 |
| **Part Two** |                               22.303 |                             22.716 |
| **TOTAL**    |                           *1718.723* |                         *2647.462* |
