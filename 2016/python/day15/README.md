# Approach
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

|              |  Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|--------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |   16824 |        1 |              20 |                   N/A |  N/A |
| **Part Two** | 3543984 |        1 |            5664 |                   N/A |  N/A |


# Original puzzle
### --- Day 15: Timing is Everything ---
The halls open into an interior plaza containing a large kinetic sculpture. The sculpture is in a sealed enclosure and seems to involve a set of identical
spherical capsules that are carried to the top and allowed to bounce through the maze of spinning pieces.

Part of the sculpture is even interactive! When a button is pressed, a capsule is dropped and tries to fall through slots in a set of rotating
discs to finally go through a little hole at the bottom and come out of the sculpture. If any of the slots aren't aligned with the capsule as it
passes, the capsule bounces off the disc and soars away. You feel compelled to get one of those capsules.

The discs pause their motion each second and come in different sizes; they seem to each have a fixed number of positions at which they stop.
You decide to call the position with the slot `0`, and count up for each position it reaches next.

Furthermore, the discs are spaced out so that after you push the button, one second elapses before the first disc is reached, and one second
elapses as the capsule passes from one disc to the one below it. So, if you push the button at `time=100`, then the capsule reaches the top
disc at `time=101`, the second disc at `time=102`, the third disc at `time=103`, and so on.

The button will only drop a capsule at an integer time - no fractional seconds allowed.

For example, at `time=0`, suppose you see the following arrangement:

```
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
```

If you press the button exactly at `time=0`, the capsule would start to fall; it would reach the first disc at `time=1`.
Since the first disc was at position `4 at `time=0`, by `time=1` it has ticked one position forward. As a five-position disc,
the next position is `0`, and the capsule falls through the slot.

Then, at `time=2`, the capsule reaches the second disc. The second disc has ticked forward two positions at this point: it started at
position `1`, then continued to position `0`, and finally ended up at position `1` again. Because there's only a slot at position `0`,
the capsule bounces away.

If, however, you wait until `time=5` to push the button, then when the capsule reaches each disc, the first disc will have ticked
forward `5+1 = 6` times (to position `0`), and the second disc will have ticked forward `5+2 = 7` times (also to position `0`).
In this case, the capsule would fall through the discs and come out of the machine.

However, your situation has more than two discs; you've noted their positions in your puzzle input.

### --- Part Two ---

After getting the first capsule (it contained a star! what great fortune!), the machine detects your success and begins to rearrange itself.

When it's done, the discs are back in their original configuration as if it were `time=0` again, but a new disc with `11` positions and starting at position `0`
has appeared exactly one second below the previously-bottom disc.
