# Approach
### Data format

I had assumed when I first read the puzzle, that I should probably just build the tree that it describes, which most
likely meant using a stack or something in order to build the nodes (since they could be nested). I put that aside and
originally just read in the list of numbers.

Now, after part 1, I came back and decided to actually build the tree. This ended up being a little tougher than I
thought, since there were no obvious delimiters and variable length nodes. But in the end, I ended up creating the tree
as a map that looks like this:

```
{
	"c": 0
	"m": 0
	"children": [
		{
			"c": 0
			"m": 0
			"children": [ ... ]
			"metas": [ ... ]
		},
		...
	],
	"metas": [ 1, 2, 3 ]
}
```
The `c` and `m` keys are simply used as counters/placeholders for the number of children/meta values that still need
added. Then each node just has a list of children and meta values.

### Part 1
> _What is the sum of all metadata entries?_

The first time I solved this, I didn't use a tree structure at all and instead just had an index pointer that moved
through the list of numbers. Since I was just trying to add up all of the meta values, the logic was pretty straightforward:

From the start:
* If the value at my current location == 0, I have no more children, so all of my next meta values are just the next `i+1` entries after the next position. Read those and move the pointer ahead that far
* If the value at my current location != 0, I have children, so I need to advance my position 2, which puts me at the start of my next child.

There were a few other use cases that needed addressed, but those could be easily ironed out. In the end, I was able to add up all the metas
pretty easily.

### Part 2
> _What is the value of the root node?_

Alright, now that I need to actually keep track of children and in the order they appear, I think it is time to actually build the tree.
I struggled with it. I kept running into issues figuring out how to get the stack to work and when to push/pop on it
because of the variable size and no clear delimiters. I knew in my head how it needed to work, but I just kept fumbling on it.

Long story short, this one was much harder than it should have been. My initial intuition was 100% correct, I just couldn't
seem to actually implement it correctly. I was hand-writing everything and debugging and stepping through line by line...

Finally I got it to build the tree as I described above. I had to maintain a counter of child/metas for each node that
I could decrement whenever I pushed a new item onto the stack and when I popped it, I'd add it to the child list.

I could probably figure out a way to make it work without maintaining the counters all the way through, but it worked.

Once I had the tree built, this part was pretty easy in that I just needed a recursive function to calculate a single node's value
exactly as described in the puzzle.

I then went back and used the new tree to solve part one, and it turns out the solutions are almost identical once you have
the tree built in a way that makes sense.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               2 |
| **Part Two** |               0 |
