# Approach
### Data format

Well, 90% of this puzzle ended up being parsing the data into a format that was most helpful. When looking at the input,
the first thought was simply to split on spaces, store everything in a 2D array and move on...but what about all the
strange spacings?!

_The left/right alignment of numbers within each problem can be ignored._

...ok, so I can ignore them for now...but why even put that line in there and have the strange spacing if it wasn't
going to be important later?

So, I did initially just store everything as numbers, but when I got to part 2, I ended up changing it so that I maintained
the spaces in every number. The way I had to do that was look at the position of the operators in the final line of the
input to help detemrine where each number ACTUALLY starts.

I then iterated over every line and saved each number, with spaces included, in my 2D array.

I finally decided to store the operation indices as well as the 2D array of numbers and return them as my data so that I could
use them in each part.

### Part 1
> _What is the grand total found by adding together all of the answers to the individual problems?_

Since I have all of the numbers in a 2D array, I decided to just rotate the array clockwise 90-degrees so that
each ROW contained the operation needed, followed by all of the numbers. This worked out well because the only
operations were `+` and `*` which are commutative. So it really doesn't matter if I read it left to right or right to left...

Now just loop over every row in my rotated matrix and get the sum or product of all of the numbers in the row based on
which operation is defined.

Very simple.

### Part 2
> _What is their similarity score?_

Well, as I mentioned in the data section above, I saved all of the spacing in the values of the array...so, I just needed
to figure out how to get the numbers correctly. The first step was to rotate the matrix again, and make sure each number in the row
had the same size, with the spaces in the correct place. So I right padded each number to the size of the longest value.
Now I had all of the numbers, with correct size and spacing, and rotated in the correct orientation.

Now, the way I built the numbers ended up building them in reverse order...so I finally just had to reverse the strings,
parse them as integers, and then I can just do the same operation(s) as I did in part 1.

It really wasn't any harder than part 1, except getting the input correct was just a pain in the...

# Results

|              |       Exec. Time (ms) - Python 3.13 | Exec. Time (ms) - PyPy 3.11 |
|--------------|------------------------------------:|----------------------------:|
| **Get Data** |                               3.152 |                       0.973 |
| **Part One** |                               3.745 |                       1.428 |
| **Part Two** |                             567.389 |                      31.018 |
| **TOTAL**    |                           *574.286* |                    *33.419* |
