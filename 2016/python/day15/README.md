# Approach
### Data format

```
Disc #{NUM} has {NUM_POS} positions; at time=0, it is at position {POS}.
```

### Part 1
> _What is the first time you can press the button to get a capsule?_

Yay, maths! What I did here was tried to figure out a formula that can represent all possible start times where the capsule
will end up falling through any given disc at a given layer. This formula ends up being:

```
let p = number of positions on the disc
let s = starting position of a disc at time=0
let l = the layer of the disc (or number of the disc)

p*(n+1) - s - l 		n ∈ N
```

This means, I can start iterating over all natural numbers, calculate the start time for each `n` for each disc and when I find a
start time that is present for all discs, then I know that would work for my time. So the easiest way I thought of to
track these times is just to create a dictionary where the valid start times are the keys and keep a count of how many discs
hit that start time. When I get a key that has a counter equal to the number of discs present, then I know I found my
ideal start time.

### Part 2
> _With this new disc, and counting again starting from time=0 with the configuration in your puzzle input, what is the first time you can press the button to get another capsule?_

Didn't have to change anything, really...just add another disc after the intial ones were loaded. It took a little bit longer,
but it wasn't too bad at just about 5 seconds.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              20 |
| **Part Two** |            5664 |
