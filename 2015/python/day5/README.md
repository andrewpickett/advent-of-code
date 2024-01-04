# Approach
### Data format

I read in each line of the input as an individual string with any whitespace removed. All stored in a single list.

### Part 1
> _How many strings are nice?_

It's really very straightforward to solve this one, because all you have to do is for each string in the input, run it
through a few regular expressions or basic rule checks to ensure it passes all of them. None of the rules are very difficult,
as they can be represented like this in pseudocode:

For a given string s:
* `if s.count("[aeiou]") >= 3`
* `if s[x] == s[x+1]` for some index `x` in the string
* if any of `['ab', 'cd', 'pq', 'xy']` are anywhere in the string

As long as all three of those are true, then it's a valid string. I originally had those all as separate checks and multiple
lines of code, but I was able to represent all of them as one long list comprehension, which was pretty slick!

### Part 2
> _How many strings are nice under these new rules?_

This part is similar to the previous, but we just had to change what the rules meant. So instead of `s[x] == s[x+1]` for
repeated letters, we have `s[x] == s[x+2]` for repeated letters one place away. We can represent the other one by iterating
over every letter in the string and getting a count of each pair of letters `s[x:x+2]`...and if it's more than one, then
it passes as well. Again, it took a little playing around, but I got it all into one comprehension!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               3 |
| **Part Two** |               4 |
