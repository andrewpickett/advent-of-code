# Approach
### Data format

I really just read each line into an array of integers, and then reversed the array so that I had the list sorted
from largest container to smallest. I threw it in an object with the target as well (made testing easier).

### Part 1
> _Filling all containers entirely, how many different combinations of containers can exactly fit all `150` liters of eggnog?_

This one screamed recursion. Just keep a list of all "valid" combinations that get you to the amount you want. You start with the largest value
first and then recursively work through them to end up with ALL combinations of numbers that amount to your value.

So using the example in the puzzle with sizes of `20`, `15`, `10`, `5`, and `5` trying to get to `25` liters, you do something like the following:
* Take largest remaining container (`20`). Since my current total (`20`) is less than my target, recursively use the remaining containers...
  * Take next largest container (`15`)...it's now too much (`35 > 25`), so ignore this and return.
  * Now try the next remaining container (`10`). Still too much, so ignore and return.
  * Try the next (`5`). It's exactly what I need. So add this as a valid combination and return.
  * Try the next (`5`). It's again exactly what I need. So add this as a valid combination and return.

I've now exhausted all possibilities using the `20` container. So we move forward in the list of containers and start with the second largest (`15`).

* Take largest (`15`). Recurse with remaining containers...
  * Next largest (`10`) gives me exactly my target, so add it and return
  * Next (`5`) gives me only a total of `20`, so I need to recurse again with any remaining
    * Pull the largest off the remaining (`5`), which now gives me exactly my total. So add it to list of valid and return.

So at this point, I've tried starting with the `20` and the `15` and found 4 possible matches:
(`20`, `5`), (`20`, `5`), (`15`, `10`) and (`15`, `5`, `5`)...

I will continue through all of the containers and find those are the only ones. But that's the general idea...run this same
algorithm on the input and you will find all valid combinations.

Once you have all possible combinations, just return the length of that array.

### Part 2
> _How many different ways can you fill that number of containers and still hold exactly `150` litres?_

For this, do the same thing as part one -- get all valid combinations. Then just count how many have a length equal to the
minimum length in the array.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              30 |
| **Part Two** |              61 |
