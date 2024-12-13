# Approach
### Data format

Intcode program -- just read the input as a list of integers that will be passed to the Intcode machine.

### Part 1
> _what diagnostic code does the program produce?_

First up was updating the `Intcode` machine. I basically take the instruction and pad it on the left with zeroes to a
length of 5. This allows me to accurately have the parameter modes for all POSSIBLE parameters of a function.

NOTE: it is possible that I'll have some unnecessary parameters sent into functions, but if they aren't used, it's no harm, no foul.

Next I added the 2 new functions -- `input` and `output`. I started with the ability for the program to actual halt and await
the user input, but then realized I don't want to have to manually intervene if I can help it. So I added an `inputs` list
to the machine so that I can supply the inputs programmatically and let the program just run.

Similarly, I added an `outputs` array to store the values whenever `output` is called.

Once I had those, I just had to set the input to the specified value, run the program, and return the last output value.

### Part 2
> _What is the diagnostic code for system ID 5?_

A few more new methods to add, but that's it. The jumps were pretty easy, since I just increment the pointer as needed
and the eq/lt operations were just like add/multiply. So really these were really simple to implement, and when I did that
I ran the program and it just worked. Nice.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
