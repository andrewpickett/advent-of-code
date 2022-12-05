# Approach
### Part 1
> _After the rearrangement procedure completes, what crate ends up on top of each stack?_

Well, I cracked the top 1000 this time, but I initially did it against how I try to do all of my puzzles. Namely, I
hardcoded some of the input in my code instead of parsing it from the input file. What I did was just create a
list of lists that I'll treat as a stacks. It looked something like this:

```python
stacks = [
	["N", "C", "R", "T", "M", "Z", "P"],
	["D", "N", "T", "S", "B", "Z"],
	["M", "H", "Q", "R", "F", "C", "T", "G"],
	["G", "R", "Z"],
	["Z", "N", "R", "H"],
	["F", "H", "S", "W", "P", "Z", "L", "D"],
	["W", "D", "Z", "R", "C", "G", "M"],
	["S", "J", "F", "L", "H", "W", "Z", "Q"],
	["S", "Q", "P", "W", "N"]
]
```

I then removed that portion of the input file, leaving just the moves listed. That allowed me to just parse the move lists
and pop/append single elements from one array to others. Because `pop()` just takes the last element, this makes the arrays
act like a stack, so everything worked as expected. In the end, I just build a string by popping the last element in each stack
and return the result.

Once I solved part 2, I decided to go back and change my code to match how I try to do all of them: I parsed everything
from the input file instead of hardcoding anything. This proved a little tricky, as I had to account for gaps in the stacks,
but in the end I like this much better, even though it's a lot more verbose with the code.

### Part 2
> _After the rearrangement procedure completes, what crate ends up on top of each stack?_

This one took a little longer -- but only because as I mentioned above, I was hardcoding the stacks in my code. This means
after part one ran, the stacks were re-arranged from their original by the time part two started. This took me a little while
to realize that I was just manipulating the same object...

I ended up writing a quick deep-copy method to get fresh data each time and then just changed my move function to use
the `extend` function instead of `append` to push whole sets of data to each stack.

When I rewrote it to parse everything from the input, I was able to remove the deep copy code as well. So everything was much
cleaner!

# Results

|              |    Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|----------:|---------:|----------------:|----------------------:|-----:|
| **Part One** | RTGWZTHLD |        1 |               5 |              00:12:17 |  833 |
| **Part Two** | STHGRZZFR |        2 |               5 |              00:13:23 | 3121 |

# Original puzzle
### --- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of
marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over,
the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the
desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will
end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

```
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
```

In this example, there are three stacks of crates. Stack 1 contains two crates: crate `Z` is on the bottom, and crate `N` is on top.
Stack 2 contains three crates; from bottom to top, they are crates `M`, `C`, and `D`. Finally, stack 3 contains a single crate, `P`.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a
different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting
in this configuration:

```
[D]
[N] [C]
[Z] [M] [P]
 1   2   3
```

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (`D`) ends up below the second and third crates:

```
        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
```

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate `C` ends up below crate `M`:

```
        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
```

Finally, one crate is moved from stack 1 to stack 2:

```
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
```

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are `C` in stack 1, `M` in stack 2, and `Z` in stack 3, so you should combine these together and give the Elves the message `CMZ`.

### --- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover
9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder,
and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

```
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
```

Moving a single crate from stack 2 to stack 1 behaves the same as before:

```
[D]
[N] [C]
[Z] [M] [P]
 1   2   3
```

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order,
resulting in this new configuration:

```
        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
```

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

```
        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
```

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate `C` that gets moved:

```
        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
```

In this example, the CrateMover 9001 has put the crates in a totally different order: `MCD`.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to
be ready to unload the final supplies.
