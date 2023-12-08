# Approach
### Part 1
> _Filling all containers entirely, how many different combinations of containers can exactly fit all `150` liters of eggnog?_

This one screamed recursion. Just keep a list of all "valid" combinations that get you to the amount you want. You start with the largest value
first and then recursively work through them to end up with ALL combinations of numbers that amount to your value.

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

# Original puzzle
### --- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - `150` liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size `20`, `15`, `10`, `5`, and `5` liters. If you need to store `25` liters, there are four ways to do it:

* `15` and `10`
* `20` and `5` (the first `5`)
* `20` and `5` (the second `5`)
* `15`, `5`, and `5`

Filling all containers entirely, how many different **combinations of containers** can exactly fit all `150` liters of eggnog?

### --- Part Two ---
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. **How many different ways** can you fill that number of containers and still hold exactly `150` litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be `3`.
