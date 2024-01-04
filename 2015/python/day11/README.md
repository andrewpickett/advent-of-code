# Approach
### Data format

Just read the input as a single string. Nothing fancy.

### Part 1
> _Given Santa's current password (your puzzle input), what should his next password be?_

This one is very similar to day 5. I took the naive approach and just actually incremented the alphabetic characters one
at a time. I then ran the new password through the rules checks to see if it's valid.
Obviously this brute force approach by itself won't be enough, so the biggest/easiest time save is the second rule:

_Passwords may not contain the letters `i`, `o`, or `l`, as these letters can be mistaken for other characters and are therefore confusing._

It's very easy to check if a string has any of those characters. If it does, we can skip all passwords until the next letter.
As an example, if we have the password `ghdizxbbcd`, we can see it has a forbidden letter (`i`). So we we can do is simply increment that letter
(to `j`) and make all following letters back to `a` for a resulting next password of `ghdjaaaaaa`. That can save massive amounts
of checks along the program.

There are obvious other shortcuts we can make with the other rules, but after making just that one change it is enough
for it to finish in just a couple seconds. So I left it there.

### Part 2
> _What's the next one?_

Just take the result from the first part and run it through the code again...

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            2242 |
| **Part Two** |            5816 |
