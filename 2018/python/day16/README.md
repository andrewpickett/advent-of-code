# Approach
### Data format

We have to read in 2 separate parts of the input file here. The first part is the samples/examples and so for those,
we can read in every 4 lines and build an object containing the "before", "after", and "instruction" pieces of the
example. Once we're done reading those in, we just need to read in each line of the remaining input as an array of
integers.

### Part 1
> _Ignoring the opcode numbers, how many samples in your puzzle input behave like three or more opcodes?_

This part is pretty simple. For each example, just run the "before" through every instruction and keep a count of
how many times the result matches the "after". Then return the number of samples that have more than 3 that matched.
All done with a single list comprehension once the operations are all stored and set up correctly.

### Part 2
> _What value is contained in register 0 after executing the test program?_

I thought it was super easy...I wrote out a mapping of for every example, which operations worked for each different
number (stored in a map). I then output the map and checked by hand if it simplified down to exactly one operation
per instruction...and I kept getting errors with it so that there were 2 numbers that could be specific instructions
as well as a couple numbers that matched no numbers. I was so confused.

I spent about an hour debugging only to find I had made `seti` and `setr` to do the exact same thing and somehow that didn't
completely mess up my part one.

Once I fixed that little error, I just ran the example program against my mapped opcodes and the answer was correct!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               7 |
| **Part Two** |               2 |
