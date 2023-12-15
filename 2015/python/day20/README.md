# Approach
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

# Original puzzle
### --- Day 20: Infinite Elves and Infinite Houses ---
To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: `1`, `2`, `3`, `4`, `5`, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

* The first Elf (number `1`) delivers presents to every house: `1`, `2`, `3`, `4`, `5`, ....
* The second Elf (number `2`) delivers presents to every second house: `2`, `4`, `6`, `8`, `10`, ....
* Elf number `3` delivers presents to every third house: `3`, `6`, `9`, `12`, `15`, ....

There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to **ten times** his or her number at each house.

So, the first nine houses on the street end up like this:
```
House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.
```
The first house gets `10` presents: it is visited only by Elf `1`, which delivers `1 * 10 = 10` presents. The fourth house gets `70` presents, because it is visited by Elves `1`, `2`, and `4`, for a total of `10 + 20 + 40 = 70` presents.

What is the **lowest house number** of the house to get at least as many presents as the number in your puzzle input?

### --- Part Two ---
The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to `50` houses. To make up for it, they decide to deliver presents equal to **eleven times** their number at each house.

With these changes, what is the new **lowest house number** of the house to get at least as many presents as the number in your puzzle input?
