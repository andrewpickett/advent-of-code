# Approach
### Data format

The way I decided to approach this was to simply keep a map of `pattern => replacement`. Pretty simple. But, what I do
is for every input pattern, I also add every rotation and flip possible for it as additional keys. This way I end up
with a fully complete map of all possible patterns. So the first step was to figure out how to determine how to do
all of the rotations/flips using just the input strings. I created helper functions for each type and just ran it through
all of them adding them to the map.

### Part 1
> _How many pixels stay on after 5 iterations?_

Alright, well, now that I have a replacement map, I decided to just approach this in a very straightforward way:
1) Take the current image and break it apart into the smaller subdivisions
2) For each subdivision, perform the substitution based on the rules map
3) Re-combine all of them back to a single image
4) Count the `#` in the final image string

It is inefficient as anything...super painful and ugly...but it worked. I'm 100% sure there's a much better/faster way
for this to be done, but I hacked it together and it worked and ran in 0ms for the first part.

### Part 2
> _How many pixels stay on after 18 iterations?_

Why not...let's just try running it 18 times instead of the original 5 and see if it could even possibly finish...

...

3 seconds. That's all. I thought there was no way it was correct, but sure enough, I entered the answer it spat out and
it was correct. So again, while it's not efficient, it worked in a decent amount of time, so I'm going to take it.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |            2562 |
