# Approach
### Part 1
> _Find the two entries that sum to 2020; what do you get if you multiply them together?_

Just like all of the previous years, this first puzzle was extremely basic.
There was no reason to get really clever or tricky on the first pass,
so I just brute forced the solution:
iterate through each pair of numbers and check their sum.

I am already seeing that I'm giong to regret doing these puzzles in core Java (no external
dependencies). Using tools like Apache Commons/Lang/etc would make a lot of this so much
faster...

So most of the time today on this was just getting the "framework" set up to read the
inputs and get my class hierarchy set up. The actual puzzle wasn't difficult.

### Part 2
> _...what is the product of the three entries that sum to 2020?_

Part 2 was just another straightforward extension on part one.
Once again, I decided to just brute force it with 3 loops.
I got the answer in about a minute and successfully finished Day 1!

