# Approach
### Data format

Just read it as a `Grid` and then make sure to set all neighbors including the diagonals on it.

### Part 1
> _What will the total resource value of the lumber collection area be after 10 minutes?_

Make a copy of the original input. Then loop over every point and re-evaluate each point, saving the result to the
copied version. At the end of the loop, assign the copied as the original, so that all changes take effect at the same
time.

I then just count the number of `|` and `#` in the resulting grid after the specified number of loops.

### Part 2
> _What will the total resource value of the lumber collection area be after 1000000000 minutes?_

Obviously we need to figure out a shortcut here. The most obvious one in this case is simply to check for any loops.
I do this by storing the grid string into an array and every generation, I check if that string already exists.
If it does, that means it will always just repeat, so since I have the repeat, I know at what point it repeats and I know
the index of the original...so I can determine the size of the repeating loop.

Then we just have to maths to determine which state would be the result at the 1000000000 minute. That math is:
```
index_of_state = loop_start + (1000000000 - loop_start) % loop_size
```

So since we already have a list of all the previous states, we can just grab the state at that index, and then count
the `|` and `#` instances. Done.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             556 |
| **Part Two** |           23669 |
