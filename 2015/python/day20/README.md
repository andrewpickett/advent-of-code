# Approach
### Data format

The input is just a number...so...read it in!

### Part 1
> _What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?_

Alright, well, this one has taken a lot of tweaking. In looking at the problem, it was clear to me that the number of presents
for any given house was simply the sum of all of their distinct factors multiplied by the 10 presents each elf delivers
(and this can be verified by looking at oeis.org for the sequence divided by 10).

So my first attempt was very rudimentary and did a simple factorization. It was slow as anything, and took 20 minutes to complete,
but it gave me the correct answer.

I then went back and optimized it quite a bit, giving an upper bound (based on the answer I got from the above slow way).

### Part 2
> _With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?_

Alright, so instead of multiplying by 10, we multiply by 11, and then we need to stop when they've delivered their 50 houses.
The math is still basically the same, so I just updated my function with those two new values and ran it.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            4600 |
| **Part Two** |            1814 |
