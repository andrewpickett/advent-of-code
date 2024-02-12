# Approach
### Data format

I really just read in each line to an array. Since I am only doing one pass of the data, I don't need to get complicated
right now. I will just instantiate "Instruction" objects as I read through them later.

### Part 1
> _What is the largest value in any register after completing the instructions in your puzzle input?_

Alright, just read through each line and do the comparison listed and increment the registers as needed. As I read a line
I initialize any new registers to 0 and then just do exactly as the instructions described. Runs really fast.

### Part 2
> _To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations._

Do the exact same thing, but this time check the value I just changed and see if it's higher than my old maximum. If so,
update the maximum and continue. At the end, just return that value.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               2 |
| **Part Two** |               2 |
