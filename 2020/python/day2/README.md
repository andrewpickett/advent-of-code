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
I went back later in the day and rewrote part 2 to use the `sum` operation as well and acutally
used the `XOR` operator (`^`) to get the solution down to one line as well!

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 580  | 1  | <1  | 00:06:58  | 1287  |
| **Part Two**  | 611  | 1  | <1  | 00:03:34  | 1107  |

# Original puzzle

### --- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via
toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers;
we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the
Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the
corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:
```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```
Each line gives the password policy and then the password. The password policy indicates the lowest and highest
number of times a given letter must appear for the password to be valid. For example, `1-3 a` means that the
password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, `cdefg`, is not; it contains no instances of `b`,
but needs at least 1. The first and third passwords are valid: they contain one `a` or nine `c`, both within the
limits of their respective policies.

How many passwords are valid according to their policies?

### --- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate
Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job
at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little
differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the
second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

* `1-3 a: abcde` is valid: position 1 contains a and position 3 does not.
* `1-3 b: cdefg` is invalid: neither position 1 nor position 3 contains `b`.
* `2-9 c: ccccccccc` is invalid: both position 2 and position 9 contain `c`.

How many passwords are valid according to the new interpretation of the policies?
