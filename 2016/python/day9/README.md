# Approach
### Data format

Read the full line as a string from the file...that's it.

### Part 1
> _What is the decompressed length of the file (your puzzle input)? Don't count whitespace._

It was really simple. Just keep a pointer on where you are in reading the input string, and whenever you see a `(`, then
parse the contents until the ending `)`. Then just move your pointer however far into the input string you copied.

Output the length of the resulting string.

**NOTE:** I ended up completely refactoring and redoing this part of the puzzle after implementing part 2. I explain the
new way in that writeup below...so for reference, this was my original part 1 code that matches my description above:

```python
def part_one():
	new_str = ""
	i = 0
	while i < len(data):
		if data[i] == "(":
			close_idx = data[i:].find(")")
			parts = data[i+1:i+close_idx].split("x")
			new_str += data[i+close_idx+1:i+close_idx+1+int(parts[0])] * int(parts[1])
			i += 1+close_idx+int(parts[0])
		else:
			new_str += data[i]
			i += 1
	return len(new_str)
```

### Part 2
> _What is the decompressed length of the file using this improved format?_

Ok, so it was obvious this was going to happen. This was the first puzzle that required a less-than-immediately-obvious
way to solve, simply due to the size of the data. I tried kicking off my original to part one, knowing -- because it explicitly
said so in the puzzle -- that it would probably never come back or my computer would crap out on it.

I was right.

So, I immediately recognized what needed to be done: recursively decompress the portions of the string, and only keep track of the
lengths instead of the actual string itself.

So, then it was just matter of actually implementing it. The idea is something like this:

Given an input string, let's call the substring BEFORE the first "(" `X`. We then have some marker (e.g. `MxN`) within parentheses.
We can use those to get the next substring which we'll call `Y`, which are the next `M` characters
after the ")". Finally, we have the last section of the string which is everything AFTER `Y`, so we'll call it `Z`.

Since we know there are no parentheses in `X`, we can move on to recursively calculating `Y` and `Z` because both of those
COULD have more markers in them. So we just need to call the same decompression on both of those. Our base case is simply when
a string has no parentheses, we can just return the length of that string.

The total length of the decompressed string then is `len(X) + (N * decompress(Y)) + decompress(Z)`

By doing that, each of those decompress calls will result in a recursive total of the substrings until it all bubbles back up
and it returns the final total.

Once I had this working for part two, I just updated the recursive function to have the option to recurse or just take one layer, which
allowed me to rewrite part one use it. That cleaned up the code quite a bit.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
