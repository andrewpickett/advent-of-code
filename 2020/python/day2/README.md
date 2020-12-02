# Approach
### Part 1
> _How many passwords are valid according to their policies??_

Another pretty straightforward puzzle, but with slightly more complicated input parsing.
I typically try to parse all of the data into the format I want upon initial read of the file,
but this one required a bit more splitting, substringing, etc. for me to figure out how to
do that quickly. Instead I just read the lines in and then did all of the parsing in my
loop.

Once you get the 4 pieces of info from each line (min occurrances, max occurrances, letter, password),
it was just looping over all of them and keeping a count of any that were valid...

Once I had the initial loop, I decided to pythonify it a bit by using `sum` to do the counting.


### Part 2
> _How many passwords are valid according to the new interpretation of the policies??_

This part of the puzzle wasn't any more difficult since the input has already been parsed.
The only "gotcha", which they were kind enough to remind you of, is that you need to
subtract 1 from the indexes (in 0-based languages) in order to do a valid check.


# Results
Overall, I still don't like my solution as I think it could be a lot cleaner and simpler,
but it works just fine.

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 580  | 1  | <1  | 00:06:58  | 1287  |
| **Part Two**  | 611  | 1  | <1  | 00:03:34  | 1107  |
