# Approach
### Data format

I read in each line of the input as an individual string with any whitespace removed. All stored in a single list.

### Part 1
> _Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?_

So. Many. Slashes.

Escaping slashes and quotes is always a ridiculous exercise. Instead I wrote out all of the rules around how the length of a string changes
whenever we run into specific characters. For example, for every `\"`, the total is 1 less. For every `\x`, the total is 3 less.
Once you write out all of the rules, it's pretty clear to see the end result is going to be

`count(") + count(\) + 3*count(\x) + 2`

the `+ 2` at the end is to include the beginning and ending quotes that we ignored when processing.

Now, the tricky part is just with writing the code to check for escaped escaped escaped characters (e.g. `\\x` would not be an escaped hex code...but `\\\x` would be...).

Either way, once you get the formula fully written out, it runs really fast.

### Part 2
> _Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal._

This is the first puzzle where the second part was MUCH easier than the first! Since every time there is a `"` or `\` in the puzzle, it
adds one new character (specifically another `"`), we can just add the number of `"` and `\` together to get the total number
newly added characters. We then would have to wrap the new string in beginning and ending `"`, meaning two additional characters.

So in the end, it's just `2 + count(") + count(\)` for each string. Really simple.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
