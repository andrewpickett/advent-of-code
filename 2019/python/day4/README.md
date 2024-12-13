# Approach
### Data format

Just read the input as a single array of 2 digits (min and max of the range).

### Part 1
> _How many different passwords within the range given in your puzzle input meet these criteria?_

Because the input already has a range constriction, there are really only 2 checks we need to make to see if a given
number is valid:
* Each digit is never decreasing
* There is at least one repeated number

So, we just do a loop over the range in the input and first check if the sorted string of the given number matches the
original -- if so, then we show the digits are never decreasing. Then we loop over the characters in the string
and just check if there are any repeats. If both are true, then we count that number as valid.

Done.

### Part 2
> _How many different passwords within the range given in your puzzle input meet all of the criteria?_

I just add one additional: basically there as to be at least one that is repeated EXACTLY twice...Other than that, the other
rules all still apply, so once I added that additional constraint, it worked just fine.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             566 |
| **Part Two** |             561 |
