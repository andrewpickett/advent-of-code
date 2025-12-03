# Approach
### Data format

Read each line in the input file as an array of integers.

### Part 1
> _what is the total output joltage?_

I REALLY need to slow down and just read the whole problem before solving. I definitely made an assumption on what I thought
it was going to be asking and coded it, not actually reading the full question. As a result, I had to write it again...

Oh well...just 10 minutes of wasted time.

I first just did a brute-force approach by doing nested for loops. It worked great and got me the right answer. However,
after reading part 2, I realized I had to re-think this one...

### Part 2
> _What is the new total output joltage?_

Ok, so just for funsies, I decided to try brute-forcing this one at first by doing 12 nested for-loops! Why not, right?!?!

Yeah, that didn't work. I waited 5 minutes and it didn't even finish the first line in the input. **shrug**

Ok, so once I decided to actually think through this, it wasn't too complicated in theory:

1. Find the maximum value on the line that is in a position that will still allow you to find enough remaining values.
2. Continue this for however many steps you need (2 for part 1, 12 for part 2).
3. When you find a value, multiply it by `10^(whatever position it's in)`

Given just that, this one SCREAMED recursion. As usual, it took a couple minutes and rewrites to get the correct base case
and recursive call, but in the end it's really quite simple.

Start at the first placeholder (`depth`) and find the maximum value in the array of numbers that still leaves enough room for all remaining values `list[:1-depth]`
Once you have that, multiply it by `10^depth` and then add it to the next recursive call, cutting the list passed in down to the remaining numbers and decreasing the depth.

It's really that simple, only a couple lines of code, and it runs relatively quickly!

This was a fun little puzzle...I actually really enjoyed it.

# Results

|              | Exec. Time (ms) - Python 3.13 |     Exec. Time (ms) - PyPy 3.11 |
|--------------|------------------------------:|--------------------------------:|
| **Get Data** |                         5.084 |                           1.110 |
| **Part One** |                         1.355 |                           0.208 |
| **Part Two** |                         4.934 |                           0.876 |
| **TOTAL**    |                      *11.373* |                         *2.194* |

** *Ran each part 20000 times and averaged the run times to get final execution time*
