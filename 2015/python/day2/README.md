# Approach
### Data format

I read in the data as a list of tuples, where each tuple is a single line from the input file. Example end result of
input is
```
[
	(1, 2, 3),
	(4, 5, 6),
	...
]
```
This allows me to just manipulate numbers easily as I go through the puzzle.

### Part 1
> _All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?_

Another very simple puzzle. The hardest part of this is just parsing the input into a format that's easily usable. I decided
to just split on each line's `x` character and map them into integers so I can do arithmetic easily. Once that is done,
it's just follow the directions exactly to add together all the combinations of the 3 numbers plus the minimum of those.

### Part 2
> _How many total feet of ribbon should they order?_

Again, since we have the numbers already usable, it's just follow the math that is outlined. Nothing tricky here.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
