# Approach
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

|              |      Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|------------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |      107035 |        1 |               0 |                   N/A |  N/A |
| **Part Two** | 11451628995 |        1 |               1 |                   N/A |  N/A |


# Original puzzle
### --- Day 9: Explosives in Cyberspace ---
Wandering around a secure area, you come across a datalink port to a new part of the network. After briefly scanning it for interesting files, you find one file in particular that catches your attention. It's compressed with an experimental format, but fortunately, the documentation for the format is nearby.

The format compresses a sequence of characters. Whitespace is ignored. To indicate that some sequence should be repeated, a marker is added to the file, like (`10x2`). To decompress this marker, take the subsequent `10` characters and repeat them `2` times. Then, continue reading the file after the repeated data. The marker itself is not included in the decompressed output.

If parentheses or other characters appear within the data referenced by a marker, that's okay - treat it like normal data, not a marker, and then resume looking for markers after the decompressed section.

For example:

* `ADVENT` contains no markers and decompresses to itself with no changes, resulting in a decompressed length of `6`.
* `A(1x5)BC` repeats only the `B` a total of `5` times, becoming `ABBBBBC` for a decompressed length of `7`.
* `(3x3)XYZ` becomes `XYZXYZXYZ` for a decompressed length of `9`.
* `A(2x2)BCD(2x2)EFG` doubles the `BC` and `EF`, becoming `ABCBCDEFEFG` for a decompressed length of `11`.
* `(6x1)(1x3)A` simply becomes `(1x3)A` - the `(1x3)` looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the `A` that comes after it. It has a decompressed length of `6`.
* `X(8x2)(3x3)ABCY` becomes `X(3x3)ABC(3x3)ABCY` (for a decompressed length of `18`), because the decompressed data from the `(8x2)` marker (the `(3x3)ABC`) is skipped and not processed further.

### --- Part Two ---
Apparently, the file actually uses version two of the format.

In version two, the only difference is that markers within decompressed data are decompressed. This, the documentation explains, provides much more substantial compression capabilities, allowing many-gigabyte files to be stored in only a few kilobytes.

For example:

* `(3x3)XYZ` still becomes `XYZXYZXYZ`, as the decompressed section contains no markers.
* `X(8x2)(3x3)ABCY` becomes `XABCABCABCABCABCABCY`, because the decompressed data from the `(8x2)` marker is then further decompressed, thus triggering the `(3x3)` marker twice for a total of six `ABC` sequences.
* `(27x12)(20x12)(13x14)(7x10)(1x12)A` decompresses into a string of `A` repeated `241920` times.
* `(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN` becomes `445` characters long.

Unfortunately, the computer you brought probably doesn't have enough memory to actually decompress the file; you'll have to come up with another way to get its decompressed length.
