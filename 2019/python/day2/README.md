# Approach
### Data format

Read the input file as an array of ints -- there are my machine's instructions. I then added a `target` and `input`
field on the data object so that I can make unit tests easier.

### Part 1
> _What value is left at position 0 after the program halts?_

So...because I know what's coming for this year (namely, that we'll have to write an entire Intcode Computer), I decided
to just start making the computer now. It's definitely overkill for this puzzle, but I made a machine that would take
the list of instructions and just run it until it hits `99`. It does this by calling different operations based on the
opcode and passes the parameters into the operation methods.

Once it's complete and no longer running, I just have to check the first element in the instructions list and return that.

...man...I'm getting anxiety just thinking about the rest of this year's puzzles...

### Part 2
> _What is 100 * noun + verb?_

Brute force. Gotta love it. Just loop from 0 to 100 for both the value for the `noun` and the `verb` and run the
Intcode program on them. If they give the expected target result, then we can just return the calculation mentioned.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |             114 |
