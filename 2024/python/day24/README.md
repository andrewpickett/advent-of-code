# Approach
### Data format

Just read the data as 2 parts - the directions and the starting values.

### Part 1
> _What decimal number does it output on the wires starting with z?_

Pretty simple simulation. Just run through all of the steps. I did make the mistake of just running through them in order
and assuming if I had an input that didn't have a value yet it was `0`...that was an incorrect assumption on my part and
rereading the puzzle pointed that out to me. So once I fixed that to just keep looping, using only values that I have
seen before, until I have processed all of them, it went smoothly.


### Part 2
> _what do you get if you sort the names of the eight wires involved in a swap and then join those names with commas?_

Manual analysis of the graph is what got me the answer. I first output the binary representation of `x+y` and `z` to see
which bits were incorrect. I then painstakingly worked through the input and graph to determine, one at a time, what
needed swapped in order to correct each bit, one at a time, starting from the least significant to the most.

I did not like this. I did not like this Sam I Am...I did not like doing this at 1:30am...

I will come back and write a general solver eventually...for now, no code for you.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               2 |
| **Part Two** |             N/A |
