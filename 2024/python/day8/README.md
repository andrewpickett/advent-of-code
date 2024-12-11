# Approach
### Data format

I started off using my `Grid`, and it worked. I got the right answers for both parts...but I ended up realizing, just like
with day 4, that I really don't need the grid, and it would be much faster just having a 2d array. So I rewrote it
to just read in the file as a 2d array of characters.


### Part 1
> _How many unique locations within the bounds of the map contain an antinode?_

I decided to just create a copy of the input data that I can manipulate by adding antinodes and not have to worry about
overwriting the actual antenna values. So basically the original array from the input is my "read" array, and the copy
ends up being my "write" array.

So now I just loop over all antenna values (I assumed all 62 possible characters are possible). If there are any that
are present more than once in the grid, I check every combination of them and get the slope between any 2 pairs of them.
From there, I can just add and subtract a slope from the two points to find the two antinodes that are created from them.
Obviously they need to be within the bounds of the grid, so I do that check as well.

Once I've looped over all antenna and added the antinodes, I just return my "write" array and count the number of `#`
in it.

### Part 2
> _How many unique locations within the bounds of the map contain an antinode?_

This is exactly the same as the first part, except that instead of just adding one antinode "before" and "after" the
two antenna in a line, we have to do a loop to continue adding them until it ends up out of bounds. So it was basically
just changing an `if` statement to a `while` statement, with the exact same conditions.

Now all of the antinodes are set, our return value is just the total number of entries that are NOT `.`. I decided
the fastest way to do this would be just subtract the number of `.` from the total entries.

Once I got the right answer, I went back and just did a little refactoring so that my `while` statement also works for the
part 1 and there is no longer any `if` statement.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              10 |
| **Part Two** |              10 |
