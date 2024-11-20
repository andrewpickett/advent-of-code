# Approach
### Data format

So, I started by actually reading in the opcode instructions...but then I realized the problem asks us to reverse
engineer. So I decided to spend some time trying to figure out what the code was actually doing and just write it
in python as my solution. So while I read in the input file, I don't actually use it at all...

### Part 1
> _What is the lowest non-negative integer value for register 0 that causes the program to halt after executing the fewest instructions?_

Well, after reverse engineering what the code is doing, I was able to just write the python to just do arithmetic
and return the result that it calculates...It's probably easier to just read my solution than explain the elf's opcode...

### Part 2
> _What is the lowest non-negative integer value for register 0 that causes the program to halt after executing the most instructions?_

Clearly we're going to be looking for a loop of some sort here, so basically run the same thing as part one, but
once we repeat a value in our fourth register, we should just return the last value, since that would've been the
upper-bound.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |              66 |
