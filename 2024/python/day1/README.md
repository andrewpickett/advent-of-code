# Approach
### Data format

We need to read the input into 2 lists -- the first number on each line, and the second number on each line. Go ahead
and sort the two lists as part of this step as well while we're at it...

### Part 1
> _What is the total distance between your lists?_

Man, I miss these early days...

Super easy: Since we've already sorted both lists as part of the `get_data` method, we can
just iterate over each element of each list and add up the absolute value of the difference between them and
return the sum. This can be done with a simple comprehension.


### Part 2
> _What is their similarity score?_

This one is actually easier than part 1! I just iterate through each element in the first list and do a `.count()` on
it in the second list. Multiply and add and there's the answer.

I got rank 788 on this one! NICE!!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              11 |
