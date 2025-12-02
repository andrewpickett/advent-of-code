# Approach
### Data format

Just read in each range by splitting the input on `,`.

### Part 1
> _What do you get if you add up all of the invalid IDs?_

Ugh...I really need to sleep. My brain was completely unable to function during this. I think I started solving part 2
while I was reading the problem, so I was making it much harder than it needed to be and it took me WAY longer than it should have to complete.

In the end, my approach was something like this:
1. Get the true range of possible values to be checking.
   1. We know invalid numbers MUST be even length, since it's a number duplicated
   2. So for the lower bound, if it's not even, then simply round up to the nearest even power of 10.
   3. For the upper bound, if it's not even, then go to the number one less than the current power of 10.
2. Now that we have the true range of possible values, if the end is lower than the start, there's nothing to do...so we only care when it's a valid range of numbers.
3. At this point, we can make a new range of numbers by taking the first half of the start of our range and the first half of the end of our range.
4. Now, we iterate over this new range and just check if the given number doubled is in the "true" range we calculated.
5. If so, add that invalid number to a set

```
Example: If the original range is 998-1012, we can do the above steps to find:
  1. Find the "true" range: 1000-1012
  2. The start is less than the end, so we can continue
  3. New range: 10-10
  4. Iterate over this new range of numbers and check if the doubled number is in our range. 1010 is in 1000-1012, so it's invalid!
  5. Add 1010 to our set of numbers
```

At the end, we are left with a set of invalid numbers, so the answer is to just return the sum. WHEW!

### Part 2
> _What do you get if you add up all of the invalid IDs using these new rules?_

Well, like I said, I was solving this part originally, so I knew what I needed to do. I pretty much do the exact same thing
as part one, but instead of doubling the value and dividing the ranges in half and everything being based on "2", I check every
amount of numbers that evenly divide the length of the values in my range! I was afraid this was going to run for a long time,
but I was pleasantly surprised to see it finish in ~1ms...so...I really didn't have to change much code to get this to work!

# Results

|              | Exec. Time (ms) - Python 3.13 | Exec. Time (ms) - PyPy 3.11 |
|--------------|------------------------------:|----------------------------:|
| **Part One** |                           1.1 |                         0.5 |
| **Part Two** |                           1.6 |                         0.5 |

