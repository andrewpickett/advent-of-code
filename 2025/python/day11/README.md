# Approach
### Data format

I started with just using a `defaultdict` to read the file and create a map exactly how it is laid out in the input.
The key was the left side of the `:` character, and the value was a `list` of all the values to the right of the `:`.

This worked fine for part one, but I made a few adjustments in order to make part2 work using my standard framework
for these puzzles. Namely, I needed to pass the dictionary into a memoized function...but that means the dictionary would
have to be immutable/hashable.

In order to accomplish this, I created a new helper class called `HashableDict` which extends the standard `dict` object
and just adds a valid `hash` method. Now to make my dictionary immutable, I changed the values to a `tuple` and couldn't
use `defaultdict` any more. It worked great, but had to use `tuple` methods while parsing.

### Part 1
> _How many different paths lead from you to out?_

This was very simple in that just start with the `you` entry in your data and add all of the values to a running list.
Now, just start popping items off of the list one at a time. Whenever you remove an `out` node, increment a counter.
If you remove any other node, just add all of that node's values to the list.

Luckily there were no loops or anything that would cause it to just run forever in this input, and it ran very fast.

### Part 2
> _How many of those paths visit both dac and fft?_

Seems very straightforward, in that you just need to pretty much the same thing as part 1, but only return a `1` if you've
visited two specific nodes before. The problem is there are a TON of possible paths with this new constraint because it starts on
`svr` instead of `you`...which goes on for eternity.

Enter memoization!

If we just use memoization and change our logic to be a recursive function, it works BEAUTIFULLY.

This puzzle went down so fast for me, I was actually quite shocked it worked so well!

# Results

|              |     Exec. Time (ms) - Python 3.13 |     Exec. Time (ms) - PyPy 3.11 |
|--------------|----------------------------------:|--------------------------------:|
| **Get Data** |                             1.465 |                           1.065 |
| **Part One** |                             1.066 |                           0.470 |
| **Part Two** |                             1.804 |                           6.377 |
| **TOTAL**    |                           *4.335* |                         *7.912* |
