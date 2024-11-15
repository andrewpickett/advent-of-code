# Approach
### Data format

Read each line as a tuple of integers.


### Part 1
> _How many constellations are formed by the fixed points in spacetime?_

Pretty straightforward. I read each value into a map where the key is the each point and the value is any other points
that are within 3 distance from the key stored as a `set`.

Once we have that, I do a super inefficient algorithm to just loop over all of the keys/values and move them around
so that if key `k` has a value `v` in the `set`, I find key `v` and move its entire set into key `k` and then remove the
key `v` completely from the map. I could certainly do this much faster, but I hacked this one together, ran it and it
gave the right answer...so, I'm good for now...

### Part 2
> __

Click a button. Done!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |           38282 |
| **Part Two** |               0 |
