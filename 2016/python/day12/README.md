# Approach
### Data format

Read each line as a space-delimited list representing each instruction. Nothing fancy here.

### Part 1
> _After executing the assembunny code in your puzzle input, what value is left in register a?_

I literally just implemented the operations as they said. The only "tricky" part is having to check if a parameter
is numeric or alphabetic. If numeric, it's just setting that value, but otherwise, you need to actually grab the value
from the register stated.

Other than that, it wasn't anything tricky.

After reaching day 23, where I needed to expand on the Assembunny code, I decided to extract it out to a separate
utility and use a more OO design. So using that, it's the same logic, but wrapped in classes.

Runs at about the same speed.

### Part 2
> _If you instead initialize register c to be 1, what value is now left in register a?_

Ran the same code, just after setting the register `c` to a value of 1. It took a while to run, which is unfortunate,
but still only took 20 seconds, so while I could go back and try to optimize, I'm not going to.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             663 |
| **Part Two** |           19928 |
