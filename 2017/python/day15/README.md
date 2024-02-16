# Approach
### Data format

Just read the inputs to a dictionary so that I can reference them. I could also have just returned a tuple, but oh well.

### Part 1
> _After 40 million pairs, what is the judge's final count?_

40,000,000 is a lot -- but not too crazy to brute force. So that's what I did. I first solved this by just running through
them one by one and doing a final modulo of 65536 (2^16) and comparing the result there. This is equivalent of checking
the lower 16 bits of two numbers. It worked fine...ran in about 30 seconds. I did go back and rewrite it using a new
`judge` method (explained below) once I finished part 2. It wasn't any faster, but it was a whole lot simpler/clearer.

### Part 2
> _After 5 million pairs, but using this new generator logic, what is the judge's final count?_

I always forget about generator functions in Python...and they're super cool. This puzzle is literally about having
2 generators, so why not use generators in Python! Basically I just create a generator for each of the two use cases.
Then I loop through 5,000,000 iterations and just get the next value for each generator and do the comparison.

I originally had tried keeping a list of values and whenever I added a new value to the list I would pop it off and compare.
It worked, but took hours to run...so clearly that wasn't ideal. This one goes MUCH faster. I'm sure I could optimize it
more, and I'm sure there's some sort of Maths shortcut with modulos and everything that would help me bypass a lot of this,
but 15 seconds isn't too bad for part 2, so I'll keep it for now.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |           30704 |
| **Part Two** |           17045 |
