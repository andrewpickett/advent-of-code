# Approach
### Data format

I ended up just taking the entire input and splitting it on the delimiter `mul`. This was a little more complicated with
the actual input, since it was 6 lines long, but after a bit of python-foo, I was able to get it down to a single
list comprehension that reads all of the lines, splits on `mul` and then combines all of the remaining tokens into a
single list.

### Part 1
> _What do you get if you add up all of the results of the multiplications?_

Since I split the input on `mul`, everything that's left in each token in my list is everything "between" `mul` tokens.

This means, "valid" tokens are those that start with `(##,##)`. It can have anything after that, but as long as it starts
with that format, it's valid. I used a regex to check if it matches that format, and any items that match this format,
just add the product of the two numbers and finally return it.


### Part 2
> _what do you get if you add up all of the results of just the enabled multiplications?_

The ONLY difference is that after doing the check for a valid token, I need to see if `do()` or `don't()` are later
in the token. If so, set a flag to whether I should process and add this flag as a condition to my validity check.

Very straightforward, in the top 1000 again. I'm happy with that.

EDIT: I realized the next morning that my solution didn't account for some specific edge cases. For example:
`mul(1,2)do()don't()mul(3,4)`
would have returned `14` because my code was just saying "if `do()` is in the next token, then count it!"...but if it was
followed by a `don't()` in the same token, it would've ignored that. So I went back and tweaked it a bit to account for this
as well.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
