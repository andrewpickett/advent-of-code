# Approach
### Data format

Just read the input as a single string. Nothing fancy.

### Part 1
> _Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?_

I'm sure there's a better way to do this, but I just did exactly what the directions say. I just kept building strings
based on the rules/numbers. It finished just fine...so I'm good with it.

### Part 2
> _Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?_

I was lazy -- I just ran the exact same code but with 50 iterations instead. It worked as it finished in <20 seconds.
I don't feel like trying to figure out the optimization here...

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            1051 |
| **Part Two** |           18277 |
