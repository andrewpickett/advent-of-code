# Approach
### Data format

I read in each line of the input as an individual string with any whitespace removed. All stored in a single list.

I would probably ideally make this more object oriented and parse each line into some sort of "Instruction" object that
can simply be run/evaluated -- but what I have works, so I don't see a need to change it. I just parse each line
as I process through it.

### Part 1
> _In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?_

This one was fun. I like these kinds of puzzles, where we are basically building an assembly language interpreter.

I didn't do anything fancy or tricky here. I really just created a dictionary to hold each of the "registers" and then
implementations for each of the different instructions. Once I run through all of the commands, just take the value at
the key of `a` in the registers and return it.

### Part 2
> _What new signal is ultimately provided to wire a?_

Ok...so just run part one's code again, take that value and set it on `b` to start, and run it again...is that really it??

...yes...yes it was...

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              89 |
| **Part Two** |             186 |
