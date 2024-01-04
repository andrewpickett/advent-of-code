# Approach
### Data format

Read the input and store it as a dictionary for the boss's statistics. It ends up looking something like this:
```
{'hp': 103, 'damage': 9, 'armor': 2}
```
I then just need to copy that for each fight

### Part 1
> _What is the least amount of gold you can spend and still win the fight?_

This was quite fun.

I hard-coded the item shop with all of the possible items you can equip (this included adding 2 "none" accessories to
account for the fact that you don't HAVE to equip any of them).

I then just ran through every combination of weapons/armor and simulated the full fight using them. If the player won,
then I add up the total cost and in the end return the minimum cost.

### Part 2
> _What is the most amount of gold you can spend and still lose the fight?_

Same thing as above, just we care about when we lose instead. So add a small condition and do the same thing.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              28 |
| **Part Two** |              29 |
