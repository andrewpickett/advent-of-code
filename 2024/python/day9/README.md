# Approach
### Data format

The end goal is to have the data saved as "blocks". Each block is simply a tuple containing the ID, and how many long it
is. I also include a flag to determine if the block has been moved or not. So when all is said and done, my resulting data
should look like this for an input of `12345`:
```
[
	(0, 1, False),
	(".", 2, False),
	(1, 3, False),
	(".", 4, False),
	(2, 5, False)
]
```
Now, in order to manipulate the blocks across the two parts, I do create copies before sending them into the functions
to be processed.

### Part 1
> _What is the resulting filesystem checksum?_

Since I have everything stored as blocks, and not individual positions in an array, I am able to shortcut a little bit
here by moving entire blocks around where possible. I keep track of the index of my current "blank" block and then
work backwards from the last block.

When processing a block from the end, there are 3 possible cases: it's longer than the blank I'm on, it's shorter than
the blank I'm on, or it's exactly the same.
* If it's exactly the same, all I do is remove the last block completely, and just rewrite the current blank with its contents.
* If it's smaller than the current blank, I just insert a new block at the position of the blank with the value at my current position and then decrement the size of the blank
* Finally, if it's larger, I replace the blank with the value at my current position, and decrement the amount at my current position to leave only what's left.

We just do this until we've gone through all of the positions at the end and filled any empty blocks. Now just run
through the checksum calculation and return the result.

### Part 2
> _What is the resulting filesystem checksum?_

So because I stored the data as blocks, this was already pretty simple to complete. In fact, this one ended up being
easier than part 1, because I just move entire blocks around instead of having to account for multiple types.

It runs a lot longer than the first part, though, because I can't increment the pointer of the first "blank" block unless
it gets completely filled. So in the case of a block only having 1 open space, it will pretty much always stay the minimum
possible, since technically SOMETHING might be able to move into it.

Either way, return the checksum again.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              87 |
| **Part Two** |            1719 |
