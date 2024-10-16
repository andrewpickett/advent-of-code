# Approach
### Data format

Just like [Day 18](../day18), this is a DuetProgram. As such, it reads the input exactly like that day's -- just a list
of instructions.

### Part 1
> _If you run the program (your puzzle input), how many times is the mul instruction invoked?_

I first had to modify the existing DuetProgram that I had written to add the new functions. I also added a step
to keep track of how many times each function was called by keeping a map inside of the DuetProgram object and just
incrementing the counters for each instruction.

Then I just ran the given input through the program and returned the "mul" operation count from that map.

### Part 2
> _After setting register a to 1, if the program were to run to completion, what value would be left in register h?_

Well, I obviously just tried setting the `a` register to `1`...clearly it didn't work -- which was expected.

So I decided to just manually write out what the program was doing on paper so I could figure out how to code a solution.
Well, no wonder it never finished -- it was going to do a loop of something like 200 trillion steps. So, I kept writing
out the algorithm and found that it all came down to the difference between registers `b` and `c` and the amount
that it increased at the end of each loop. Long story short, I just wrote a quick nested for-loop to actually do the
calculation and it worked.

Ideally, I'd like to figure out a more programmatic way to do this, but for now, it works. I did at least grab the
initialization values and step values from the input.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             100 |
| **Part Two** |             948 |
